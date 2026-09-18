#!/usr/bin/env python3
"""Doc health checks for mkdocs-void (DOCS_WIKI_PLAN.md, Phase 1).

Verifies, from the repo root:

1. No ``docs/**`` page or README links to, embeds, or references any PLAN file
   (Rule 11: PLAN.md, WHY_PLAN.md, RENAME-PLAN.md, DOCS_WIKI_PLAN.md).
2. Every relative intra-doc ``.md`` link resolves from the page's directory.
3. Screenshot contract: every ``Screenshots/*.png`` referenced in docs exists,
   and every shipped screenshot is referenced somewhere in the docs.
4. Config-surface contract: every inline-code ``theme.void.*``, ``theme.*`` and
   ``extra.void_*`` key used in the docs exists in the plugin's canonical
   surfaces (``_VOID_TOKEN_MAP``, ``_void_defaults``, the top-level ``void``
   keys the plugin reads, and the ``extra.void_*`` keys templates read).
5. One ``# H1`` per page (code fences stripped); no ``TODO``/``FIXME``.
6. Nav reconciliation: every docs page (except ``not_in_nav``) appears in
   ``mkdocs.yml`` ``nav``, and every nav target resolves to a real file.

Run from the repo root:

    python tools/check_docs.py

Only PyYAML (already required by MkDocs) is needed; the config-surface check
imports ``void.plugins.void_plugin`` and is skipped with a note if the theme
environment is not installed. Exit codes: 0 = healthy, 1 = violations.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SHOTS = ROOT / "Screenshots"
THEME_DIR = ROOT / "void"

PLAN_FILES = ("PLAN.md", "WHY_PLAN.md", "RENAME-PLAN.md", "DOCS_WIKI_PLAN.md")

KNOWN_THEME_KEYS = {
    "name",
    "logo",
    "favicon",
    "language",
    "direction",
    "palette",
    "font",
    "features",
    "custom_dir",
    "icon",
    "analytics",
}

# -- regexes ---------------------------------------------------------------

PLAN_LINK = re.compile(
    r"\]\((?:[^()]|\([^()]*\))*?("
    + "|".join(re.escape(p) for p in PLAN_FILES)
    + r")[^)]*\)",
    re.I,
)
MD_LINK = re.compile(r"\]\(([^)]+?)\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,}).*$")
BACKTICK = re.compile(r"`([^`\n]+)`")
CONFIG_KEY = re.compile(
    r"(theme\.void\.[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*"
    r"|theme\.[A-Za-z_][A-Za-z0-9_]*"
    r"|extra\.void_[A-Za-z0-9_]+)"
)
H1 = re.compile(r"^#\s+\S.+$", re.M)
TODO = re.compile(r"\bTODO\b|\bFIXME\b", re.I)
SHOT_REF = re.compile(r"Screenshots/([\w.\-]+\.png)")

# -- helpers ---------------------------------------------------------------


def _strip_code(text: str) -> str:
    """Remove fenced code-block interiors so fences never break checks."""
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
        elif not in_fence:
            out.append(line)
    return "\n".join(out)


def _target(link: str) -> str:
    return link.split("#", 1)[0].split("?", 1)[0].strip()


# -- checks ----------------------------------------------------------------


def check_plan_links() -> list[str]:
    bad = []
    for page in sorted(list(DOCS.rglob("*.md")) + list(ROOT.rglob("README*.md"))):
        if "site" in page.parts:
            continue
        if PLAN_LINK.search(page.read_text(encoding="utf-8")):
            bad.append(f"{page.relative_to(ROOT)}: links/embeds a PLAN file")
    return bad


def check_doc_links() -> list[str]:
    bad = []
    for page in DOCS.rglob("*.md"):
        if page.name == "_config_ref.generated.md":
            continue
        text = _strip_code(page.read_text(encoding="utf-8"))
        for link in MD_LINK.findall(text):
            if "://" in link or link.startswith(("#", "mailto:")):
                continue
            target = _target(link)
            if not target.lower().endswith(".md"):
                continue
            rel = page.parent / target
            if not rel.exists() and not (DOCS / target).exists():
                bad.append(f"{page.relative_to(ROOT)} -> {target}")
    return bad


def check_screenshots() -> list[str]:
    referenced = set()
    for page in DOCS.rglob("*.md"):
        referenced.update(SHOT_REF.findall(page.read_text(encoding="utf-8")))
    actual = {p.name for p in SHOTS.glob("*.png")} if SHOTS.exists() else set()
    bad = []
    bad += [
        f"Screenshots/{name} referenced but missing"
        for name in sorted(referenced - actual)
    ]
    bad += [
        f"Screenshots/{name} shipped but never referenced in docs"
        for name in sorted(actual - referenced)
    ]
    return bad


def _config_surface():
    """Derive the canonical config surfaces from the plugin + templates."""
    import void.plugins.void_plugin as plugin

    source = Path(plugin.__file__).read_text(encoding="utf-8")
    token_groups = {
        group: set(mapping) for group, mapping in plugin._VOID_TOKEN_MAP.items()
    }
    top_level = set(plugin.VoidPlugin._void_defaults)
    top_level.update(token_groups)

    top_level.update(re.findall(r"""void\[\s*["'](\w+)["']\s*\]""", source))
    top_level.update(re.findall(r"""void\s*=\s*void\.get\(\s*["'](\w+)["']""", source))

    extra_keys = set(re.findall(r'extra\[\s*["\']void_(\w+)["\']\s*\]', source))
    extra_keys.update(re.findall(r'extra\.get\(\s*["\']void_(\w+)["\']', source))
    extra_keys.update(re.findall(r"""["']void_(\w+)["']""", source))
    for tmpl in THEME_DIR.rglob("*.html"):
        extra_keys.update(
            re.findall(r"extra\.void_(\w+)", tmpl.read_text(encoding="utf-8"))
        )
    return token_groups, top_level, extra_keys


def check_config_keys() -> list[str]:
    try:
        token_groups, top_level, extra_keys = _config_surface()
    except Exception as exc:  # noqa: BLE001 - env missing; skip loudly
        print(f"note: config-surface check skipped ({exc})", file=sys.stderr)
        return []

    bad = []
    for page in DOCS.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        for span in BACKTICK.findall(text):
            m = CONFIG_KEY.search(span)
            if not m:
                continue
            parts = m.group(1).split(".")
            if parts[0] == "theme" and parts[1] == "void":
                if len(parts) < 3:
                    continue  # bare `theme.void` namespace mention
                first, rest = parts[2], parts[3:]
                if first not in top_level:
                    bad.append(
                        f"{page.name}: unknown theme.void.{first}.{'.'.join(rest)}"
                    )
                elif (
                    first in token_groups
                    and rest
                    and rest[0] not in token_groups[first]
                ):
                    bad.append(
                        f"{page.name}: unknown token theme.void.{first}.{rest[0]}"
                    )
            elif parts[0] == "theme" and parts[1] not in KNOWN_THEME_KEYS:
                bad.append(f"{page.name}: unknown theme.{parts[1]}")
            elif parts[0] == "extra" and parts[1][5:] not in extra_keys:
                bad.append(f"{page.name}: unknown extra.{parts[1]}")
    return bad


def check_h1_and_todos() -> list[str]:
    bad = []
    for page in DOCS.rglob("*.md"):
        if page.name == "_config_ref.generated.md":
            continue
        text = _strip_code(page.read_text(encoding="utf-8"))
        count = len(H1.findall(text))
        if count != 1:
            name = page.relative_to(ROOT)
            bad.append(f"{name}: {count} H1 (want exactly 1)")
        if TODO.search(page.read_text(encoding="utf-8")):
            bad.append(f"{page.relative_to(ROOT)}: contains TODO/FIXME")
    return bad


def check_nav() -> list[str]:
    import yaml

    doc = yaml.compose((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    if doc is None:
        return ["mkdocs.yml is empty"]
    pairs = list(doc.value)
    nav_node = next((n for n in pairs if n[0].value == "nav"), None)
    not_in_node = next((n for n in pairs if n[0].value == "not_in_nav"), None)
    not_in_nav = set(not_in_node[1].value.split()) if not_in_node else set()
    targets: set[str] = set()

    def walk(node) -> None:
        if isinstance(node, yaml.SequenceNode):
            for child in node.value:
                walk(child)
            return
        if not isinstance(node, yaml.MappingNode):
            return
        for key, value in node.value:
            if isinstance(value, yaml.ScalarNode):
                targets.add(value.value)
            elif isinstance(value, yaml.SequenceNode):
                walk(value)

    if nav_node is not None:
        walk(nav_node[1])

    bad = []
    for target in sorted(
        t for t in targets if not t.startswith(("http://", "https://"))
    ):
        if not (DOCS / target).exists():
            bad.append(f"nav -> {target}: file missing")
    for page in DOCS.rglob("*.md"):
        rel = str(page.relative_to(DOCS)).replace("\\", "/")
        if rel in not_in_nav:
            continue
        if rel not in targets:
            bad.append(
                f"{rel}: present in docs/ but missing from nav (add to nav or not_in_nav)"
            )
    return bad


def main() -> int:
    checks = [
        ("PLAN-file links (Rule 11)", check_plan_links),
        ("intra-doc links", check_doc_links),
        ("screenshot contract", check_screenshots),
        ("config keys used in docs", check_config_keys),
        ("one H1 + no TODO/FIXME", check_h1_and_todos),
        ("docs <-> nav reconciliation", check_nav),
    ]
    failures: list[str] = []
    for label, fn in checks:
        found = fn()
        if found:
            failures.extend(found)
            print(f"[FAIL] {label}")
            for line in found:
                print(f"   - {line}")
        else:
            print(f"[ ok ] {label}")
    if failures:
        print(f"\n{len(failures)} doc-health violation(s) found")
        return 1
    print("\ndoc health OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
