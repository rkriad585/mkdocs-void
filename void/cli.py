# Copyright (c) 2025 rkriad585 contributors

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""Void command-line interface.

`void new [TARGET]` creates a working Void docs project (mkdocs.yml +
docs/index.md) from the full commented project template — theme, palette,
plugin, markdown extensions and every tuning surface — ready for
`mkdocs serve`. Placeholders in the template are filled from the target
name and the repository detected in the current directory.

`void doctor [--config-file FILE]` audits the current project and prints a
health report: mkdocs + void versions, `site_url`, theme, fonts, node, and
the service-worker cache version. Exits 0 on a healthy project, 1 when a
check fails, and 2 on usage or YAML errors.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

from . import __version__ as _VOID_CLI_VERSION

NEW_PROJECT_TEMPLATE = (
    Path(__file__).resolve().parent / "templates" / "project" / "mkdocs.yml"
)

INDEX_TEMPLATE = "# Welcome\n\nBuilt with Void.\n"

USAGE = "usage: void new [TARGET] | doctor [--config-file FILE]"
DOCTOR_USAGE = "usage: void doctor [--config-file FILE]  (default: mkdocs.yml in the current directory)"


def main(argv=None) -> int:
    args = list(argv) if argv is not None else sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(USAGE)
        return 0
    command = args[0]
    if command == "new":
        return _cmd_new(args[1:])
    if command == "doctor":
        return _cmd_doctor(args[1:])
    print(
        f"void: unknown command {command!r} (expected 'new' or 'doctor')",
        file=sys.stderr,
    )
    print(USAGE, file=sys.stderr)
    return 2


def _slug(name: str) -> str:
    """Turn a project name into a repo-friendly slug (e.g. \"My Docs\" -> my-docs)."""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-").lower()
    return slug or "my-docs"


def _repo_username() -> str:
    """Best-effort GitHub owner for the repo_url placeholder."""
    try:
        origin = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        ).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return "your-username"
    match = re.search(r"[:/]([^/:]+)/[^/:]+(?:\.git)?$", origin)
    return match.group(1) if match else "your-username"


def _cmd_new(argv) -> int:
    target = Path(argv[0]) if argv else Path(".")
    if (target / "mkdocs.yml").exists():
        print(
            f"refusing to overwrite existing project at {target}",
            file=sys.stderr,
        )
        return 1
    slug = _slug(target.name) if argv else "my-docs"

    body = NEW_PROJECT_TEMPLATE.read_text(encoding="utf-8")
    body = body.replace("{REPO_USERNAME}", _repo_username())
    body = body.replace("{PROJECTS_NAME}", slug)
    files = {
        "mkdocs.yml": body,
        "docs/index.md": INDEX_TEMPLATE,
    }

    for name, content in files.items():
        p = target / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    print(f"Void project scaffolded at {target}. Run: mkdocs serve")
    return 0


def _sw_cache_versions(sw_text: str):
    static = re.search(r'CACHE_STATIC\s*=\s*"([^"]+)"', sw_text)
    cdn = re.search(r'CACHE_CDN\s*=\s*"([^"]+)"', sw_text)
    return (
        static.group(1) if static else None,
        cdn.group(1) if cdn else None,
    )


def _cmd_doctor(argv) -> int:
    import mkdocs  # imported lazily so `void new` stays light
    from mkdocs.utils.yaml import (
        yaml_load,
    )  # MkDocs' loader handles !ENV and !!python/name tags
    from yaml import YAMLError

    config_file = "mkdocs.yml"
    if argv and argv[0] in ("-h", "--help"):
        print(DOCTOR_USAGE)
        return 0
    if argv:
        if argv[0] == "--config-file":
            if len(argv) < 2:
                print(
                    "void doctor: --config-file requires a path",
                    file=sys.stderr,
                )
                return 2
            config_file = argv[1]
        else:
            print(f"void doctor: unknown option {argv[0]!r}", file=sys.stderr)
            print(DOCTOR_USAGE, file=sys.stderr)
            return 2

    fails = 0
    warns = 0
    print(f"mkdocs {mkdocs.__version__}  void {_VOID_CLI_VERSION}")

    config_path = Path(config_file)
    if not config_path.exists():
        print(
            f"[fail] config file not found: {config_path} (run void doctor from the project root)",
        )
        return 1
    with config_path.open("r", encoding="utf-8") as fh:
        try:
            data = yaml_load(fh) or {}
        except YAMLError as exc:
            print(f"[fail] {config_path} is not valid YAML: {exc}")
            return 2

    site_url = str(data.get("site_url") or "").strip()
    if site_url:
        print(f"[ok] site_url: {site_url}")
    else:
        warns += 1
        print("[warn] site_url is empty - set it in mkdocs.yml before going live")

    theme = data.get("theme") or {}
    if theme.get("name") == "void":
        print("[ok] theme.name: void")
    else:
        fails += 1
        print(f"[fail] theme.name is {theme.get('name')!r} - expected 'void'")

    font = theme.get("font") or {}
    font_text = font.get("text") or "Space Grotesk"
    font_code = font.get("code") or "Space Mono"
    print(f"[ok] fonts: text={font_text} code={font_code}")

    plugins = data.get("plugins") or []
    has_void = any(
        p == "void" or (isinstance(p, dict) and "void" in p) for p in plugins
    )
    if has_void:
        print("[ok] plugins include the void plugin")
    else:
        warns += 1
        print("[warn] the `void` plugin is not enabled - add it under `plugins:`")

    node = shutil.which("node")
    if node:
        proc = subprocess.run(
            [node, "--version"], capture_output=True, text=True, check=False
        )
        node_ver = (proc.stdout or "").strip() or "unknown"
        print(f"[ok] node: {node_ver}")
    else:
        warns += 1
        print(
            "[warn] node not found - install Node.js to rebuild the theme CSS (`npm run build`)",
        )

    package_sw = Path(__file__).resolve().parent / "templates" / "sw.js"
    if package_sw.exists():
        static_v, cdn_v = _sw_cache_versions(package_sw.read_text(encoding="utf-8"))
        site_sw = Path("site") / "sw.js"
        if site_sw.exists():
            s_static, s_cdn = _sw_cache_versions(site_sw.read_text(encoding="utf-8"))
            if (s_static, s_cdn) == (static_v, cdn_v):
                print(
                    f"[ok] sw.js cache versions match the theme (static={static_v}, cdn={cdn_v})",
                )
            else:
                warns += 1
                print(
                    f"[warn] site/sw.js is stale (site static={s_static}, cdn={s_cdn}; "
                    f"theme static={static_v}, cdn={cdn_v}) - rebuild with `mkdocs build`",
                )
        else:
            print(
                f"[ok] sw.js cache versions (static={static_v}, cdn={cdn_v}) - "
                "build the site to register it",
            )

    extra = data.get("extra") or {}
    version_buster = extra.get("void_version")
    if version_buster:
        print(f"[ok] extra.void_version: {version_buster}")
    else:
        warns += 1
        print("[warn] extra.void_version is not set - assets ship with ?v=1")

    if fails:
        print(
            f"void doctor: {fails} problem(s), {warns} warning(s) - project is not healthy"
        )
        return 1
    if warns:
        print(f"void doctor: {warns} warning(s), 0 problems - project is healthy")
        return 0
    print("void doctor: project is healthy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
