"""Local publication preflight. Review manifests bind exact bytes, not identity."""

import hashlib
from html import unescape
import json
from pathlib import Path
import re
from urllib.parse import unquote

from catalog import PagesError

TEXT = {".html", ".htm", ".css", ".js", ".mjs", ".json", ".txt", ".md", ".mmd",
        ".xml", ".csv", ".tsv", ".yaml", ".yml", ".svg"}
EMAIL = re.compile(r"(?i)[a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)+")
PRIVATE_HOST = re.compile(r"(?i)\b(?:[a-z0-9-]+\.)+(?:internal|corp|local|bilibili\.co)(?![a-z0-9.-])")
CREDENTIAL = re.compile(
    r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----|\b(?:github_pat_[A-Za-z0-9_]{20,}|"
    r"gh[pousr]_[A-Za-z0-9]{24,}|sk-(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[A-Z0-9]{16})\b"
    r"|(?i:\b(?:authorization\s*[:=]\s*[\x22\x27]?bearer\s+[A-Za-z0-9._~-]{12,}))"
)
OPAQUE = re.compile(r"(?i)\bdata\s*:|<\s*(?:iframe|embed|object|canvas|video|audio)\b")


def scan_text(text, location):
    for value in {text, unquote(unescape(text))}:
        if CREDENTIAL.search(value):
            raise PagesError(f"Public preflight blocked: credential-like content in {location}")
        if PRIVATE_HOST.search(value):
            raise PagesError(f"Public preflight blocked: internal hostname in {location}")
        for match in EMAIL.finditer(value):
            domain = match.group().rsplit("@", 1)[1].lower()
            if domain not in {"example.com", "example.net", "example.org"} and not domain.endswith((".example", ".invalid", ".test")):
                raise PagesError(f"Public preflight blocked: non-example email in {location}")


def review_inputs(files, metadata):
    """Return only assets requiring visual/manual review. Never log raw matches."""
    for value in metadata:
        if value:
            scan_text(value, "publication metadata")
    review = {}
    for name, data in files.items():
        scan_text(name, "an asset filename")
        ext = Path(name).suffix.lower()
        try:
            decoded = data.decode("utf-8") if ext in TEXT else None
        except UnicodeDecodeError:
            decoded = None
        text = decoded if decoded is not None and "\x00" not in decoded else None
        if text is not None:
            scan_text(text, name)
        if text is None or ext == ".svg" or OPAQUE.search(text):
            review[name] = hashlib.sha256(data).hexdigest()
    return review


def require_review(expected, manifest):
    if manifest is not None:
        try:
            result = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise PagesError("Cannot read --reviewed-assets manifest") from exc
        if not isinstance(result, dict) or result != {"reviewed_assets": expected}:
            raise PagesError("Reviewed assets do not match current files; regenerate and review the new snapshot")
    elif expected:
        raise PagesError("Public preflight blocked: assets require review; run preflight, then pass --reviewed-assets")
