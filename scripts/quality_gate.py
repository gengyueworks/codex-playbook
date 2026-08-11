#!/usr/bin/env python3
"""Quality gate for the Codex field guide."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def markdown_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]


def check_chapters() -> None:
    zh = sorted((ROOT / "playbook" / "zh").glob("*.md"))
    en = sorted((ROOT / "playbook" / "en").glob("*.md"))
    if len(zh) != 10 or len(en) != 10:
        fail(f"expected 10 chapters per language, found zh={len(zh)} en={len(en)}")
    for path in zh + en:
        text = path.read_text(encoding="utf-8")
        if text.count("```") % 2:
            fail(f"unclosed code fence: {path.relative_to(ROOT)}")
        if "#" not in text:
            fail(f"missing heading: {path.relative_to(ROOT)}")
    print("PASS: chapter counts and Markdown fences")


def check_sensitive_content() -> None:
    # Keep the maintained vocabulary out of this source file while checking it at runtime.
    forbidden = [
        "\u53ef\u6284",
        "\u503c\u5f97\u6284",
        "\u6284\u539f\u5219",
        "/" + "Volumes" + "/",
        "/" + "Users" + "/",
        "/" + "tmp" + "/",
    ]
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for term in forbidden:
            if term in text:
                fail(f"sensitive content {term!r}: {path.relative_to(ROOT)}")
    print("PASS: sensitive content scan")


def check_links() -> None:
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in markdown_files():
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("/"):
                continue
            candidate = (path.parent / unquote(target)).resolve()
            if not candidate.exists():
                fail(f"broken link in {path.relative_to(ROOT)}: {target}")
    print("PASS: local Markdown links")


def check_examples() -> None:
    for relative in (
        "examples/03-source-collection/input/sample-bookmarks.json",
        "examples/en/03-source-collection/input/sample-bookmarks.json",
    ):
        with (ROOT / relative).open(encoding="utf-8") as handle:
            json.load(handle)
    print("PASS: example JSON")


def check_tables() -> None:
    for path in markdown_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines[:-2]):
            if not line.strip().startswith("|") or not line.rstrip().endswith("|"):
                continue
            if lines[index + 1].strip():
                continue
            if lines[index + 2].strip().startswith("|"):
                fail(f"blank line inside table: {path.relative_to(ROOT)}:{index + 1}")
    print("PASS: table spacing")


def main() -> None:
    check_chapters()
    check_sensitive_content()
    check_links()
    check_examples()
    check_tables()
    print("QUALITY_GATE_OK")


if __name__ == "__main__":
    main()

