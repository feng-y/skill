"""Prepare report copies and render the site catalog without rewriting source HTML."""

from html import escape, unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from string import Template
from urllib.parse import quote, urlsplit

from catalog import (
    UNCATEGORIZED, PagesError, available_topic_id, exact_entry, parse_timestamp, relative_path, validate_catalog,
)


BACK_START = "<!-- to-pages:back-link:start -->"
BACK_END = "<!-- to-pages:back-link:end -->"
HOME_MARKER = "<!-- to-pages:managed-index -->"
HOME_PREFIX = ("<!doctype html>\n" + HOME_MARKER + "\n").encode("utf-8")
HOME_PREFIX_CRLF = HOME_PREFIX.replace(b"\n", b"\r\n")
CHARSET = '<meta charset="utf-8">'
BACK_LINK = """
<style>
#to-pages-back-link {
  position: fixed; z-index: 10000;
  right: max(1rem, env(safe-area-inset-right));
  bottom: max(1rem, env(safe-area-inset-bottom));
  display: inline-flex; align-items: center; gap: .45em;
  min-height: 44px; box-sizing: border-box; padding: .55em .9em;
  border: 1px solid #b4d5cd; border-radius: .65em;
  background: #173a36; color: #fff; text-decoration: none;
  font: 600 14px/1.2 system-ui, sans-serif;
  box-shadow: 0 3px 14px #13282140;
}
#to-pages-back-link:hover { background: #23534d; }
#to-pages-back-link:focus-visible {
  outline: 2px solid #fff; outline-offset: 2px; box-shadow: 0 0 0 6px #173a36;
}
@media print { #to-pages-back-link { display: none !important; } }
</style>
<a id="to-pages-back-link" href="$href" data-site-path="$site_path" target="_self"><span aria-hidden="true">←</span>返回导航</a>
<script>
(() => {
  const link = document.getElementById("to-pages-back-link");
  const home = new URL(link.dataset.sitePath, window.location.href);
  const referrer = document.referrer && new URL(document.referrer);
  if (referrer && referrer.origin === home.origin && referrer.pathname === home.pathname) {
    home.search = referrer.search;
  }
  link.href = home.href;
})();
</script>
"""


class MissingBaseURL(ValueError):
    pass


class Document(HTMLParser):
    """Collect metadata and source offsets so edits leave the original markup intact."""

    CDATA_CONTENT_ELEMENTS = (
        "script", "style", "title", "textarea", "xmp", "iframe", "noembed", "noframes", "noscript",
    )

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.line_offsets = [0] + [match.end() for match in re.finditer("\n", text)]
        self.doctype_end = 0
        self.tag_ends = {}
        self.tag_closes = {}
        self.encodings = []
        self.has_base_href = False
        self.back_links = []
        self.back_start = None
        self.inert = []
        self.raw_start = None
        self.title = ""
        self.description = ""
        self.heading = ""
        self.saw_title = False
        self.saw_heading = False
        self.reading_heading = False
        self.feed(text)
        self.link_fallback = len(text)
        if self.inert:
            self.link_fallback = self.inert[0][1]
        elif self.cdata_elem:
            self.link_fallback = self.raw_start
        if not self.cdata_elem and self.rawdata.startswith("<!--"):
            self.link_fallback = min(self.link_fallback, len(text) - len(self.rawdata))
        else:
            self.close()

    def source_offset(self):
        line, column = self.getpos()
        return self.line_offsets[line - 1] + column

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype") and not self.doctype_end:
            self.doctype_end = self.source_offset() + len(decl) + 3

    def handle_starttag(self, tag, attrs):
        start = self.source_offset()
        if tag in self.CDATA_CONTENT_ELEMENTS:
            self.raw_start = start
        if tag in ("template", "svg", "math"):
            self.inert.append((tag, start))
        if self.inert:
            return
        if tag in ("html", "head"):
            self.tag_ends.setdefault(tag, start + len(self.get_starttag_text()))
        if tag == "base" and any(name == "href" for name, _ in attrs):
            self.has_base_href = True
        if tag == "meta":
            attrs = dict(attrs)
            charset = attrs.get("charset")
            if charset is None and (attrs.get("http-equiv") or "").lower() == "content-type":
                match = re.search(r"""\bcharset\s*=\s*['"]?([\w-]+)""", attrs.get("content") or "", re.I)
                charset = match[1] if match else None
            if charset is not None:
                self.encodings.append((start, start + len(self.get_starttag_text()), charset.lower()))
            if not self.description and (attrs.get("name") or "").lower() == "description":
                self.description = " ".join((attrs.get("content") or "").split())
        if tag == "h1" and not self.saw_heading:
            self.saw_heading = self.reading_heading = True

    def handle_endtag(self, tag):
        if self.inert:
            if tag == self.inert[-1][0]:
                self.inert.pop()
            return
        if tag in ("body", "html"):
            self.tag_closes.setdefault(tag, self.source_offset())
        if tag == "title":
            self.saw_title = True
        if tag == "h1":
            self.reading_heading = False

    def handle_data(self, data):
        if self.inert:
            return
        if self.cdata_elem == "title" and not self.saw_title:
            self.title += unescape(data)
        if self.reading_heading and not self.cdata_elem:
            self.heading += data

    def handle_comment(self, data):
        if self.inert:
            return
        start = self.source_offset()
        if self.text.startswith(BACK_START, start):
            self.back_start = start
        elif self.back_start is not None and self.text.startswith(BACK_END, start):
            self.back_links.append((self.back_start, start + len(BACK_END)))
            self.back_start = None


def prepare_html(data: bytes, base_url: str) -> bytes:
    text = data.decode("utf-8")
    document = Document(text)
    edits = []
    encodings = [
        (start, end, charset) for start, end, charset in document.encodings
        if not any(link_start <= start < link_end for link_start, link_end in document.back_links)
    ]
    _, charset_end, charset = next(iter(encodings), (0, 0, None))
    if charset != "utf-8" or len(text[:charset_end].encode("utf-8")) > 1024:
        bom_end = int(text.startswith("\ufeff"))
        candidates = (
            document.tag_ends.get("head"),
            document.tag_ends.get("html"),
            document.doctype_end or bom_end,
        )
        charset_at = next((offset for offset in candidates if offset is not None
                           and len(text[:offset].encode("utf-8")) + len(CHARSET) <= 1024),
                          candidates[-1])
        edits.append((charset_at, charset_at, CHARSET))
        edits.extend((start, end, "") for start, end, _ in encodings)
        if not bom_end and len(text[:charset_at].encode("utf-8")) + len(CHARSET) > 1024:
            # A long prologue can put the declaration past the browser's prescan.
            edits.append((0, 0, "\ufeff"))

    site_path = "/" + urlsplit(base_url).path.strip("/")
    site_path = quote(site_path.rstrip("/") + "/", safe="/%!$&'()*+,;=:@")
    href = site_path
    if document.has_base_href:
        if not base_url:
            raise MissingBaseURL("contains <base href> and requires cloudflare.base_url")
        href = base_url.rstrip("/") + "/"
    link = Template(BACK_LINK).substitute(href=escape(href), site_path=escape(site_path))
    link = BACK_START + link + BACK_END
    if document.back_links:
        start, end = document.back_links[0]
        edits.append((start, end, link))
        edits.extend((start, end, "") for start, end in document.back_links[1:])
    else:
        link_at = document.tag_closes.get("body", document.tag_closes.get("html", document.link_fallback))
        edits.append((link_at, link_at, link))

    chunks = []
    cursor = 0
    for start, end, replacement in sorted(edits, key=lambda edit: edit[:2]):
        chunks.extend((text[cursor:start], replacement))
        cursor = end
    chunks.append(text[cursor:])
    return "".join(chunks).encode("utf-8")


def report_details(data: bytes, path: str) -> tuple[str, str]:
    document = Document(data.decode("utf-8", errors="replace"))
    title = " ".join(document.title.split())
    heading = " ".join(document.heading.split())
    return title or heading or path, document.description or (heading if heading != title else "")


def archive_topics(site_root: Path, catalog: dict | None) -> list[dict]:
    registered = catalog["topics"] if catalog is not None else []
    known_paths = {version["path"] for topic in registered for version in topic["versions"]}
    known_ids = {topic["id"] for topic in registered}
    topics = list(registered)
    for directory, children, files in os.walk(site_root):
        folder = Path(directory)
        children[:] = sorted(name for name in children
                             if not name.startswith(".") and name not in ("node_modules", "__pycache__")
                             and not (folder / name).is_symlink())
        entry = folder / "index.html"
        if folder == site_root or "index.html" not in files or entry.is_symlink() or not entry.is_file():
            continue
        path = folder.relative_to(site_root).as_posix()
        if path in known_paths:
            continue
        try:
            relative_path(path)
        except PagesError:
            continue
        title, description = report_details(entry.read_bytes(), path)
        topic_id = available_topic_id(path, known_ids)
        known_ids.add(topic_id)
        topics.append({"id": topic_id, "title": title, "description": description, "category": UNCATEGORIZED,
                       "project": "", "versions": [{"path": path, "label": "v1", "published_at": None,
                                                    "updated_at": None, "summary": ""}]})

    archive = []
    for topic in topics:
        versions = []
        newest_registrations_first = reversed(topic["versions"])
        for version in sorted(newest_registrations_first,
                              key=lambda item: date_key(item["published_at"]), reverse=True):
            path = version["path"]
            stamp = version["updated_at"] or version["published_at"]
            versions.append({"path": path, "href": "./" + quote(path, safe="/") + "/",
                             "label": version["label"], "date": stamp, "summary": version["summary"]})
        updated = max((version["date"] for version in versions), key=date_key)
        archive.append({**topic, "updated": updated, "versions": versions})
    archive.sort(key=lambda topic: (topic["id"], topic["versions"][0]["path"]))
    archive.sort(key=lambda topic: date_key(topic["updated"]), reverse=True)
    return archive


def date_key(value):
    stamp = parse_timestamp(value)
    return stamp is not None, stamp


def static_topics(topics):
    cards = []
    for topic in topics:
        title = escape(topic["title"])
        latest = topic["versions"][0]
        description = escape(topic["description"])
        details = f'<p class="doc-description">{description}</p>' if description else ""
        links = "".join(
            f'<li><a href="{escape(version["href"])}">{escape(version["label"])}</a></li>'
            for version in topic["versions"]
        )
        history = f"<ul>{links}</ul>" if len(topic["versions"]) > 1 else ""
        cards.append(
            f'<li><a href="{escape(latest["href"])}"><h2>{title}</h2></a>{details}'
            f'<p class="project">{escape(topic["category"])} · {escape(latest["path"])}/</p>{history}</li>'
        )
    return "\n".join(cards)


def render_homepage(site_root: Path, *, adopt: bool = False, catalog: dict | None = None) -> bytes | None:
    """Return generated bytes for a missing or managed homepage, or None for a custom one."""
    index = exact_entry(site_root / "index.html")
    if index.is_symlink() or (index.exists() and not index.is_file()):
        return None
    if index.is_file() and not adopt:
        with index.open("rb") as existing:
            if not existing.read(len(HOME_PREFIX_CRLF)).startswith((HOME_PREFIX, HOME_PREFIX_CRLF)):
                return None
    if catalog is not None:
        validate_catalog(catalog, site_root)

    topics = archive_topics(site_root, catalog)
    data = json.dumps(topics, ensure_ascii=True, sort_keys=True, separators=(",", ":")).replace("<", r"\u003c")
    template = Template(Path(__file__).with_name("navigation.html").read_text(encoding="utf-8"))
    return template.substitute(marker=HOME_MARKER, count=len(topics), cards=static_topics(topics), data=data).encode("utf-8")
