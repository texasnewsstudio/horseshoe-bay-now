#!/usr/bin/env python3
"""Build sitemap.xml from published HTML files in this repository."""
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://horseshoebaynow.com"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)
urlset = ET.Element(f"{{{NS}}}urlset")
for file in sorted(ROOT.rglob("*.html")):
    rel = file.relative_to(ROOT)
    if any(part.startswith(".") or part in {"node_modules", "vendor", "tests"} for part in rel.parts):
        continue
    loc = BASE + ("/" if str(rel) == "index.html" else "/" + rel.as_posix())
    item = ET.SubElement(urlset, f"{{{NS}}}url")
    ET.SubElement(item, f"{{{NS}}}loc").text = loc
    result = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel.as_posix()], cwd=ROOT, text=True, capture_output=True)
    if result.stdout.strip():
        ET.SubElement(item, f"{{{NS}}}lastmod").text = result.stdout.strip()
ET.indent(urlset, space="  ")
(ROOT / "sitemap.xml").write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(urlset, encoding="utf-8") + b"\n")
