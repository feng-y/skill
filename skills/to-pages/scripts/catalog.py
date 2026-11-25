"""Validate and update the Git-tracked report catalog."""

from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re


CATALOG_PATH = Path(".to-pages/catalog.json")
UNCATEGORIZED = "未分类"
TOPIC_FIELDS = {"id", "title", "description", "category", "project", "versions"}
VERSION_FIELDS = {"label", "path", "published_at", "updated_at", "digest", "summary"}
UTC_TIMESTAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|\+00:00)")


class PagesError(Exception):
    pass


def relative_path(value, allow_root=False):
    if not isinstance(value, str) or not value:
        raise PagesError("Expected a nonempty relative path")
    if value == "." and allow_root:
        return value
    if any(ord(char) < 32 or 0xD800 <= ord(char) <= 0xDFFF for char in value) or any(
        not part.strip() or part.startswith(".") or part in ("node_modules", "__pycache__")
        or "\\" in part for part in value.split("/")
    ):
        raise PagesError("Paths must be relative, without hidden or parent components")
    return value


def content_digest(files: dict[str, bytes]) -> str:
    hashes = {name: sha256(data).hexdigest() for name, data in files.items()}
    return sha256(json.dumps(hashes, sort_keys=True).encode("ascii")).hexdigest()


def parse_timestamp(value):
    if value is None:
        return None
    if isinstance(value, str) and UTC_TIMESTAMP.fullmatch(value):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            pass
    raise PagesError("Catalog dates must be ISO UTC timestamps or null")


def directory_path(repo: Path, path: str) -> Path:
    current = repo
    for part in Path(path).parts:
        current = current / part
        if current.is_symlink() or (current.exists() and not current.is_dir()):
            raise PagesError("Destination contains a symlink or a file where a directory is required")
    return current


def catalog_file(repo: Path) -> Path:
    path = directory_path(repo, CATALOG_PATH.parent.as_posix()) / CATALOG_PATH.name
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise PagesError("Catalog must be a regular file without symlinks")
    return path


def check_text(value, field, *, required=False):
    if not isinstance(value, str) or (required and not value.strip()) or any(
        (ord(char) < 32 and char not in "\n\t") or 0xD800 <= ord(char) <= 0xDFFF for char in value
    ):
        raise PagesError(f"Invalid catalog {field}")
    if field in ("id", "label") and ("\n" in value or "\t" in value):
        raise PagesError(f"Invalid catalog {field}")


def validate_catalog(catalog: dict, site_root: Path):
    if not isinstance(catalog, dict) or set(catalog) != {"schema", "output_dir", "topics"}:
        raise PagesError("Invalid catalog fields")
    if type(catalog["schema"]) is not int or catalog["schema"] != 1:
        raise PagesError("Unsupported catalog schema")
    relative_path(catalog["output_dir"], allow_root=True)
    if not isinstance(catalog["topics"], list):
        raise PagesError("Catalog topics must be a list")

    ids = set()
    paths = set()
    for topic in catalog["topics"]:
        if not isinstance(topic, dict) or set(topic) != TOPIC_FIELDS:
            raise PagesError("Invalid catalog topic fields")
        for field in TOPIC_FIELDS - {"versions"}:
            check_text(topic[field], field, required=field in ("id", "title", "category"))
        if topic["id"] in ids:
            raise PagesError("Duplicate catalog topic id")
        ids.add(topic["id"])
        if not isinstance(topic["versions"], list) or not topic["versions"]:
            raise PagesError("Catalog topic requires at least one version")

        labels = set()
        for version in topic["versions"]:
            if not isinstance(version, dict) or set(version) != VERSION_FIELDS:
                raise PagesError("Invalid catalog version fields")
            check_text(version["label"], "label", required=True)
            check_text(version["summary"], "summary")
            if not isinstance(version["digest"], str) or not re.fullmatch(r"[0-9a-f]{64}", version["digest"]):
                raise PagesError("Invalid catalog content digest")
            published, updated = (parse_timestamp(version[field]) for field in ("published_at", "updated_at"))
            if published and updated and updated < published:
                raise PagesError("Catalog update precedes publication")
            path = relative_path(version["path"])
            if path in paths or version["label"] in labels:
                raise PagesError("Duplicate catalog path or topic version label")
            paths.add(path)
            labels.add(version["label"])
            entry = directory_path(site_root, path) / "index.html"
            if entry.is_symlink() or not entry.is_file():
                raise PagesError("Catalog version requires an existing index.html without symlinks")


def unique_json_fields(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PagesError("Duplicate catalog JSON field")
        result[key] = value
    return result


def load_catalog(repo: Path, output_dir: str) -> dict:
    site_root = directory_path(repo, relative_path(output_dir, allow_root=True))
    path = catalog_file(repo)
    if not path.exists():
        return {"schema": 1, "output_dir": output_dir, "topics": []}
    try:
        catalog = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_json_fields)
    except (ValueError, RecursionError) as exc:
        raise PagesError("Catalog is not valid UTF-8 JSON") from exc
    validate_catalog(catalog, site_root)
    if catalog["output_dir"] != output_dir:
        raise PagesError("Catalog output_dir does not match cloudflare.output_dir")
    return catalog


def write_catalog(repo: Path, catalog: dict) -> bool:
    if not isinstance(catalog, dict):
        raise PagesError("Invalid catalog fields")
    site_root = directory_path(repo, relative_path(catalog.get("output_dir"), allow_root=True))
    validate_catalog(catalog, site_root)
    path = catalog_file(repo)
    data = (json.dumps(catalog, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if path.exists() and load_catalog(repo, catalog["output_dir"]) == catalog:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def available_topic_id(path, ids):
    topic_id = path
    suffix = 2
    while topic_id in ids:
        topic_id = f"{path}-{suffix}"
        suffix += 1
    return topic_id


def update_catalog(catalog, path, files, *, changed, title, description, metadata):
    for field, value in metadata.items():
        if value is not None:
            check_text(value, {"topic": "id", "version": "label"}.get(field, field),
                       required=field not in ("project", "summary"))
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z") if changed else None
    topics = {topic["id"]: topic for topic in catalog["topics"]}
    for topic in topics.values():
        version = next((v for v in topic["versions"] if v["path"] == path), None)
        if version is not None:
            if metadata["topic"] not in (None, topic["id"]) or metadata["version"] not in (None, version["label"]):
                raise PagesError("Report path already belongs to another topic or version label")
            break
    else:
        topic_id = metadata["topic"] or available_topic_id(path, topics)
        topic = topics.get(topic_id)
        if topic is None:
            topic = {"id": topic_id, "title": title, "description": description,
                     "category": UNCATEGORIZED, "project": "", "versions": []}
            catalog["topics"].append(topic)

        labels = {v["label"] for v in topic["versions"]}
        label = metadata["version"]
        if label in labels:
            raise PagesError("Version label already belongs to another report path")
        if label is None:
            numbers = (int(name[1:]) for name in labels if re.fullmatch(r"v[1-9][0-9]*", name))
            label = f"v{max(numbers, default=0) + 1}"
        version = {"path": path, "label": label, "published_at": now, "updated_at": None,
                   "summary": "", "digest": None}
        topic["versions"].append(version)

    for field in ("title", "category", "project"):
        if metadata[field] is not None:
            topic[field] = metadata[field]
    if metadata["summary"] is not None:
        version["summary"] = metadata["summary"]
    if changed:
        version["updated_at"] = now
    if changed or version["digest"] is None:
        version["digest"] = content_digest(files)
