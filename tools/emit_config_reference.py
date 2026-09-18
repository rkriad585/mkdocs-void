"""Emit the canonical Void config reference from the plugin's own source.

Phase 3 (DOCS_WIKI_PLAN.md) - Configuration Bible.

Walks the real `void_plugin` constants (`_VOID_TOKEN_MAP`, `_void_defaults`,
and every `_VOID_DEFAULT_*` module dict), plus the compiled token defaults in
`void/templates/assets/stylesheets/void.scss`, and writes *complete* markdown
pages - one per config group - with a per-key section, a stable anchor, and a
Default / CSS variable / Purpose / Example table. It also writes a kitchen-sink
`mkdocs.yml` fragment with every option set to its shipped default.

Everything is derived from source tables, so docs can never drift from code.
Output is deterministic (no timestamps); CI verifies it with `--check`.

Run from the repo root:

    python tools/emit_config_reference.py            # write pages + sink
    python tools/emit_config_reference.py --check    # exit 1 if anything drifts
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - guarded at runtime
    yaml = None

REPO_ROOT = Path(__file__).resolve().parent.parent
SCSS = REPO_ROOT / "void" / "templates" / "assets" / "stylesheets" / "void.scss"
OUT_DIR = REPO_ROOT / "docs" / "getting-started" / "configuration"
SINK_FILE = OUT_DIR / "_kitchen_sink.generated.yml"

HEADER = "<!-- generated: do not edit. Run `python tools/emit_config_reference.py`. -->"

# Human titles for the default dicts, matching the config sections users know.
DEFAULT_TITLES = {
    "_VOID_DEFAULT_KEYBOARD": "keyboard",
    "_VOID_DEFAULT_READING_MODE": "reading_mode",
    "_VOID_DEFAULT_ACTION_CLUSTER": "action_cluster",
    "_VOID_DEFAULT_CONFIG_BUILDER": "config_builder",
    "_VOID_DEFAULT_TIMER": "timer",
    "_VOID_DEFAULT_CONTENT": "content",
    "_VOID_DEFAULT_AI_READER": "ai_reader",
    "_VOID_DEFAULT_SOCIAL_CARDS": "social_cards",
    "_VOID_DEFAULT_META": "meta",
    "_VOID_DEFAULT_FEEDBACK": "feedback",
    "_VOID_DEFAULT_ANNOUNCEMENT_BAR": "announcement_bar",
    "_VOID_DEFAULT_COOKIE_CONSENT": "cookie_consent",
    "_VOID_DEFAULT_COMMENTS": "comments",
    "_VOID_DEFAULT_I18N": "i18n",
    "_VOID_DEFAULT_BREADCRUMBS": "breadcrumbs",
    "_VOID_DEFAULT_PWA": "pwa",
    "_VOID_DEFAULT_ASSETS": "assets",
}

# Hand-maintained one-line "Purpose" and a copyable "Example" per key. Keys are
# dotted theme.void paths; values are (purpose, example) tuples. Everything else
# is documented purely from source (Default + CSS variable), so this stays small.
NOTES: dict[str, tuple[str, str]] = {
    "glass": (
        "Glass intensity: backdrop blur, saturation and panel opacity.",
        'glass: "medium"   # "light" | "medium" | "heavy" | "none"',
    ),
    "dot_matrix": (
        "Toggles the dot-matrix NothingOS canvas behind the content.",
        "dot_matrix: true",
    ),
    "animation": (
        "Entrance and hover animation intensity.",
        'animation: "normal"   # "normal" | "reduced" | "none"',
    ),
    "border": (
        "Glass panel border weight.",
        'border: "thin"   # "thin" | "thick" | "none"',
    ),
    "highlight": (
        "Master switch for syntax highlighting (highlight.js).",
        "highlight: true",
    ),
    "notes": ("Master switch for the notes panel feature.", "notes: true"),
    "colors.primary": (
        "Accent color for active states, links and progress.",
        'colors: {primary: "#ff3030"}',
    ),
    "colors.background": (
        "Page/canvas background color token.",
        'colors: {background: "#000000"}',
    ),
    "colors.surface": (
        "Glass panel background color token.",
        'colors: {surface: "rgba(255, 255, 255, 0.08)"}',
    ),
    "colors.text": ("Primary text color token.", 'colors: {text: "#ffffff"}'),
    "colors.border": (
        "Glass panel border color token.",
        'colors: {border: "rgba(255, 255, 255, 0.18)"}',
    ),
    "typography.font_family": (
        "Body font stack. Drives --void-font-body.",
        'typography: {font_family: "Space Grotesk"}',
    ),
    "typography.font_family_mono": (
        "Code font stack. Drives --void-font-mono.",
        'typography: {font_family_mono: "Space Mono"}',
    ),
    "typography.font_size_base": (
        "Base font size for article text.",
        'typography: {font_size_base: "16px"}',
    ),
    "spacing.sidebar_width": (
        "Sidebar rail width.",
        'spacing: {sidebar_width: "260px"}',
    ),
    "spacing.toc_width": (
        "Table-of-contents rail width.",
        'spacing: {toc_width: "220px"}',
    ),
    "spacing.content_max_width": (
        "Article column max width.",
        'spacing: {content_max_width: "720px"}',
    ),
    "border_radius.small": (
        "Small element corner radius.",
        'border_radius: {small: "4px"}',
    ),
    "border_radius.medium": (
        "Medium element corner radius.",
        'border_radius: {medium: "8px"}',
    ),
    "border_radius.large": (
        "Large element corner radius.",
        'border_radius: {large: "12px"}',
    ),
    "transitions.duration": (
        "Default transition duration.",
        'transitions: {duration: "300ms"}',
    ),
    "transitions.easing": (
        "Default transition easing curve.",
        'transitions: {easing: "cubic-bezier(0.4, 0, 0.2, 1)"}',
    ),
    "shadows.small": (
        "Small elevation shadow.",
        'shadows: {small: "0 1px 2px rgba(0, 0, 0, 0.3)"}',
    ),
    "components.header.show": (
        "Shows/hides the header rail. See the before/after pair below.",
        "components: {header: {show: true}}",
    ),
    "components.sidebar.show": (
        "Shows/hides the sidebar rail. See the before/after pair below.",
        "components: {sidebar: {show: true}}",
    ),
    "components.toc.show": (
        "Shows/hides the TOC rail. See the before/after pair below.",
        "components: {toc: {show: true}}",
    ),
    "components.footer.show": (
        "Shows/hides the footer. See the before/after pair below.",
        "components: {footer: {show: true}}",
    ),
    "components.content.show": (
        "Shows/hides the article column. See the before/after pair below.",
        "components: {content: {show: true}}",
    ),
    "components.search.show": (
        "Shows/hides the header search trigger. See the before/after pair below.",
        "components: {search: {show: true}}",
    ),
    "components.notes.show": (
        "Shows/hides the notes panel trigger. See the before/after pair below.",
        "components: {notes: {show: true}}",
    ),
    "components.admonitions.show": (
        "Turns admonitions styling on/off. See the before/after pair below.",
        "components: {admonitions: {show: true}}",
    ),
    "components.mermaid.show": (
        "Turns mermaid diagram rendering on/off. See the before/after pair below.",
        "components: {mermaid: {show: true}}",
    ),
    "components.math.show": (
        "Turns KaTeX math rendering on/off. See the before/after pair below.",
        "components: {math: {show: true}}",
    ),
    "components.highlighting.show": (
        "Turns code highlighting on/off. See the before/after pair below.",
        "components: {highlighting: {show: true}}",
    ),
    "components.code.show_copy_button": (
        "Copy button on fenced code blocks. Set false to hide the button.",
        "components: {code: {show_copy_button: true}}",
    ),
    "components.repo_popover.fields": (
        "Which repository info sections the header popover renders (empty = none).",
        "components: {repo_popover: {fields: [description, stars, language]}}",
    ),
    "keyboard.enabled": (
        "Master switch for the keyboard shortcut system.",
        "keyboard: {enabled: true}",
    ),
    "keyboard.shortcuts.search.key": (
        "Key that opens full-screen search.",
        "keyboard: {shortcuts: {search: {key: /}}}",
    ),
    "keyboard.shortcuts.toggle_sidebar.key": (
        "Key that folds/expands the sidebar.",
        "keyboard: {shortcuts: {toggle_sidebar: {key: Ctrl+Shift+B}}}",
    ),
    "reading_mode.enabled": (
        "Master switch for distraction-free reading mode.",
        "reading_mode: {enabled: true}",
    ),
    "reading_mode.shortcut_key": (
        "Key that enters/leaves reading mode.",
        "reading_mode: {shortcut_key: Alt+Shift+R}",
    ),
    "action_cluster.enabled": (
        "Master switch for the floating plus action cluster.",
        "action_cluster: {enabled: true}",
    ),
    "action_cluster.position": (
        "Which corner the floating cluster pins to.",
        'action_cluster: {position: "bottom-left"}',
    ),
    "timer.enabled": (
        "Master switch for the built-in focus timer.",
        "timer: {enabled: true}",
    ),
    "timer.default_minutes": (
        "Default focus session length in minutes.",
        "timer: {default_minutes: 25}",
    ),
    "content.show_progress_bar": (
        "Toggles the top-edge reading progress bar.",
        "content: {show_progress_bar: true}",
    ),
    "content.typography.image_lightbox": (
        "Toggles click-to-zoom image preview in the article.",
        "content: {typography: {image_lightbox: true}}",
    ),
    "config_builder.enabled": (
        "Dev tool that generates mkdocs.yml from a guided form. Ships OFF on purpose.",
        "config_builder: {enabled: false, url: assets/config-builder.html}",
    ),
    "ai_reader.enabled": (
        "Master switch for the watermarked markdown mirrors AI agents can fetch.",
        "ai_reader: {enabled: true}",
    ),
    "social_cards.enabled": (
        "Master switch for JSON-LD + auto OG cards.",
        "social_cards: {enabled: true}",
    ),
    "meta.enabled": (
        "Master switch for the last-updated + edit-on-GitHub bar.",
        "meta: {enabled: true}",
    ),
    "meta.date_source": (
        "Where the 'Last updated' date comes from.",
        'meta: {date_source: "auto"}',
    ),
    "feedback.enabled": (
        "Master switch for the 'Was this page helpful?' widget (opens an issue).",
        "feedback: {enabled: true}",
    ),
    "announcement_bar.enabled": (
        "Opt-in announcement card. Renders only when enabled and text is set.",
        "announcement_bar: {enabled: true, text: New in v0.2, position: top}",
    ),
    "announcement_bar.position": (
        "Floating placement of the announcement card.",
        'announcement_bar: {position: "top"}   # top | right | bottom | left | center',
    ),
    "cookie_consent.render": (
        "When the consent banner renders: only with an integration, always, or never.",
        'cookie_consent: {render: "auto"}   # "auto" | "always" | "never"',
    ),
    "comments.enabled": (
        "Opt-in giscus comments. Requires repo + repo_id to actually render.",
        "comments: {enabled: true}",
    ),
    "comments.mapping": (
        "How a page maps to a giscus discussion.",
        'comments: {mapping: "pathname"}',
    ),
    "breadcrumbs.show": (
        "Toggles the breadcrumb trail above the article.",
        "breadcrumbs: {show: true}",
    ),
    "pwa.manifest": (
        "Auto-generates manifest.webmanifest so the site is installable.",
        "pwa: {manifest: true}",
    ),
    "pwa.display": ("PWA display mode.", 'pwa: {display: "standalone"}'),
    "assets.mode": (
        "Library loading mode: cdn (default), self-hosted local, or concatenated bundle.",
        'assets: {mode: "cdn"}   # "cdn" | "local" | "bundle"',
    ),
    "assets.inline_critical_css": (
        "Inline the critical subset of the theme CSS into the HTML head.",
        "assets: {inline_critical_css: false}",
    ),
}

# Components whose `*.show` switch gets a rendered with/without screenshot pair
# (only the visibly switchable surfaces).
TOGGLE_SHOTS = (
    "header",
    "sidebar",
    "toc",
    "footer",
    "mermaid",
    "math",
    "highlighting",
)

# Deterministic top-level pages: (filename, page title).
PAGES = (
    ("tokens.md", "Configuration - basics & design tokens"),
    ("components.md", "Configuration - components"),
    ("shortcuts.md", "Configuration - shortcuts & interaction"),
    ("content.md", "Configuration - content & AI"),
    ("site.md", "Configuration - site, integrations & PWA"),
    ("i18n.md", "Configuration - i18n UI strings"),
)


def _scss_defaults() -> dict[str, str]:
    """Resolve `--var: value` declarations from the compiled-source SCSS."""
    raw = SCSS.read_text(encoding="utf-8")
    decls = {
        m.group(1): m.group(2).strip()
        for m in re.finditer(r"--([\w-]+)\s*:\s*([^;]+);", raw)
    }

    def resolve(var: str, depth: int = 0) -> str | None:
        if depth > 3:
            return None
        value = decls.get(var.lstrip("-"))
        if value is None:
            return None
        match = re.fullmatch(r"var\((--[\w-]+)\)", value.strip())
        if match:
            return resolve(match.group(1), depth + 1)
        return value.strip()

    resolved: dict[str, str] = {}
    for var, value in decls.items():
        found = resolve(var)
        if found is not None:
            resolved["--" + var] = found
    return resolved


def _fmt(value) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=True)
    if yaml is not None:
        text = yaml.safe_dump(value, sort_keys=True, default_flow_style=True).strip()
        return " ".join(text.splitlines())
    return repr(value)


def _flatten(mapping: dict, prefix: tuple[str, ...] = ()):
    for key in sorted(mapping):
        value = mapping[key]
        path = prefix + (key,)
        if isinstance(value, dict):
            yield from _flatten(value, path)
        else:
            yield path, value


def _anchor(path: tuple[str, ...]) -> str:
    return "themevoid" + "".join(str(part).lower() for part in path)


def _toc_line(paths) -> str:
    return " &middot; ".join(f"[{'.'.join(p)}](#{_anchor(p)})" for p in paths)


def _rows(path: tuple[str, ...], value, css_var: str | None) -> list[tuple[str, str]]:
    rows = [("Default", f"`{_fmt(value)}`")]
    if css_var:
        rows.append(("CSS variable", f"`{css_var}`"))
    note = NOTES.get(".".join(path))
    if note:
        purpose, example = note
        rows.append(("Purpose", purpose))
        rows.append(("Example", f"`{example}`"))
    return rows


def _table(rows: list[tuple[str, str]]) -> str:
    return "| | |\n|---|---|\n" + "\n".join(f"| {k} | {v} |" for k, v in rows)


def _screenshot_block(path: tuple[str, ...]) -> str:
    name = path[0]
    rel = "../../Screenshots"
    return (
        "| State | Screenshot |\n"
        "|---|---|\n"
        f"| On (default) | ![`{name}` on]({rel}/components-{name}-on.png) |\n"
        f"| Off | ![`{name}` off]({rel}/components-{name}-off.png) |\n"
    )


def _build_sections(plugin, filename: str) -> list[tuple[str, list]]:
    """Return [(section_title, [(path, value, css_var), ...])] for a page."""
    sections: list[tuple[str, list]] = []
    if filename == "tokens.md":
        sections.append(
            (
                "Basics",
                [
                    (p, v, None)
                    for p, v in _flatten(dict(plugin.VoidPlugin._void_defaults))
                ],
            )
        )
        defaults = _scss_defaults()
        for group, mapping in sorted(plugin._VOID_TOKEN_MAP.items()):
            sections.append(
                (
                    group,
                    [
                        ((group, key), defaults.get(css, css), css)
                        for key, css in sorted(mapping.items())
                    ],
                )
            )
    elif filename == "components.md":
        sections.append(
            (
                "components",
                [
                    (p, v, None)
                    for p, v in _flatten(dict(plugin._VOID_DEFAULT_COMPONENTS))
                ],
            )
        )
    else:
        names = {
            "shortcuts.md": ("keyboard", "reading_mode", "action_cluster", "timer"),
            "content.md": ("content", "config_builder", "ai_reader"),
            "site.md": (
                "social_cards",
                "meta",
                "feedback",
                "announcement_bar",
                "cookie_consent",
                "comments",
                "breadcrumbs",
                "pwa",
                "assets",
            ),
            "i18n.md": ("i18n",),
        }[filename]
        for name in names:
            const = next(k for k, v in DEFAULT_TITLES.items() if v == name)
            sections.append(
                (
                    name,
                    [
                        ((name, *p), v, None)
                        for p, v in _flatten(dict(getattr(plugin, const)))
                    ],
                )
            )
    return sections


def _emit_page(filename: str, title: str, plugin) -> str:
    head = (
        "---\n"
        f"title: {title}\n"
        "---\n\n"
        f"# {title}\n\n"
        "Generated from the live plugin tables (`_VOID_TOKEN_MAP`, "
        "`_void_defaults`, the `_VOID_DEFAULT_*` dicts and the compiled token "
        "defaults in `void.scss`) by `tools/emit_config_reference.py`. The page "
        "is regenerated in CI and can never drift from the shipped code.\n\n"
        f"{HEADER}\n\n"
    )
    body: list[str] = []
    for section_title, items in _build_sections(plugin, filename):
        body.append(f"## {section_title}\n\n")
        body.append(f"- {_toc_line([p for p, _, _ in items])}\n\n")
        for path, value, css_var in items:
            child = ".".join(path)
            body.append(f"### `theme.void.{child}`\n")
            body.append(_table(_rows(path, value, css_var)) + "\n\n")
            if filename == "components.md" and _is_show_shot(path):
                body.append(_screenshot_block(path) + "\n")
    return head + "".join(body)


def _is_show_shot(path: tuple[str, ...]) -> bool:
    return len(path) == 2 and path[1] == "show" and path[0] in TOGGLE_SHOTS


def _emit_sink(plugin) -> str:
    out = [
        "# Kitchen-sink mkdocs.yml override - every theme.void option set to its",
        "# shipped default. Copy what you need and remove the rest.",
        "theme:",
        "  name: void",
        "  void:",
    ]
    indent = "    "
    covered: set[str] = set()

    blocks: list[tuple[str, dict, str]] = [
        ("Basics", dict(plugin.VoidPlugin._void_defaults), ""),
        (
            "components",
            {"components": dict(plugin._VOID_DEFAULT_COMPONENTS)},
            "components",
        ),
    ]
    defaults = _scss_defaults()
    for group, mapping in sorted(plugin._VOID_TOKEN_MAP.items()):
        blocks.append(
            (
                f"Design tokens - {group}",
                {group: {k: defaults.get(css, css) for k, css in mapping.items()}},
                group,
            )
        )
    for const, section_title in DEFAULT_TITLES.items():
        blocks.append(
            (
                section_title,
                {section_title: dict(getattr(plugin, const))},
                section_title,
            )
        )

    for banner, mapping, dotted in blocks:
        out.append("")
        out.append(f"{indent}# {'-' * 4} {banner}")
        _emit_yaml_map(out, mapping, indent, covered, dotted)
    return "\n".join(out) + "\n"


def _emit_yaml_map(
    out: list[str],
    mapping: dict,
    indent: str,
    covered: set[str],
    dotted: str = "",
) -> None:
    for key in sorted(mapping):
        value = mapping[key]
        path = f"{dotted}.{key}" if dotted else key
        if dotted and path in covered:
            continue
        comment = ""
        note = NOTES.get(path)
        if note and len(note[1]) < 60:
            comment = f"  # {note[1]}"
        if isinstance(value, dict):
            out.append(f"{indent}{key}:{comment}")
            _emit_yaml_map(out, value, indent + "  ", covered, path)
            if dotted:
                covered.add(path)
        else:
            covered.add(path)
            out.append(f"{indent}{key}: {_yaml_scalar(value)}{comment}")


def _yaml_scalar(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=True)
    return json.dumps(value, ensure_ascii=True)


def _load_plugin():
    import void.plugins.void_plugin as plugin

    return plugin


def _build_outputs() -> dict[Path, str]:
    plugin = _load_plugin()
    outputs: dict[Path, str] = {}
    for filename, title in PAGES:
        outputs[OUT_DIR / filename] = _emit_page(filename, title, plugin)
    outputs[SINK_FILE] = _emit_sink(plugin)
    return outputs


def main(argv: list[str] | None = None) -> int:
    args = list(argv) if argv is not None else sys.argv[1:]
    check_only = "--check" in args
    if yaml is None:
        raise SystemExit("PyYAML is required to regenerate the config reference")

    outputs = _build_outputs()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    drifted = []
    for path, text in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if check_only:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                drifted.append(str(path.relative_to(REPO_ROOT)))
        else:
            path.write_text(text, encoding="utf-8")
            print(
                f"wrote {path.relative_to(REPO_ROOT)} ({len(text.splitlines())} lines)"
            )

    if check_only:
        if drifted:
            print(f"error: {len(drifted)} generated reference(s) are stale:")
            for name in drifted:
                print(f"  - {name}  (run python tools/emit_config_reference.py)")
            return 1
        print("config reference is current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
