"""Capture before/after screenshot pairs for the component toggle switches.

For every `.show` toggle listed in TOGGLES (keys below
`theme.void.components.*`), builds a small demo project twice -- once with the
defaults ("on", shared across toggles) and once with `show: false` -- then
saves a full-page PNG as `Screenshots/components-<name>-on.png` and
`Screenshots/components-<name>-off.png`. The components reference page
(`docs/getting-started/configuration/components.md`) embeds these pairs, and
`tools/check_docs.py` enforces that every referenced file exists.

Run by a maintainer when the theme's chrome changes; the results are committed.
"""

from __future__ import annotations

import argparse
import http.server
import os
import shutil
import socketserver
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "docs" / "Screenshots"
TEMP = Path(os.environ.get("TEMP", ROOT)) / "toggle_demo"

TOGGLES = [
    "header",
    "sidebar",
    "toc",
    "footer",
    "mermaid",
    "math",
    "highlighting",
]

DEMO_INDEX = """\
# Toggle demo

A page long enough to exercise every chrome surface: the header with search and
notes controls, the sidebar nav, the table-of-contents rail, the article column
with admonitions, diagrams, math and highlighted code, and a footer.

## Section one

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vitae libero ac
tellus aliquam posuere. Mauris interdum erat a fermentum venenatis.

!!! note
    Admonitions use the NothingOS glass treatment.

!!! warning
    A second admonition to make the styling unmistakable.

## Section two

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Inline math \\(a^2 + b^2 = c^2\\) and display math:

$$ \
\\int_{-\\infty}^{\\infty} e^{-x^2}\\,dx = \\sqrt{\\pi}
$$

```mermaid
graph LR
    A[Void] --> B[Glass]
    A --> C[Matrix]
    A --> D[Mono]
```

## Section three

- First list item
- Second list item
- Third list item

| Key | Meaning |
|-----|---------|
| `glass` | Backdrop blur intensity |
| `dot_matrix` | Background texture |

Paragraphs of filler so the page scrolls and the footer sits below the fold.
More filler. More filler. More filler. More filler. More filler. More filler.
"""

BASE_CONFIG = """\
site_name: Toggle Demo
site_url: https://example.invalid/
theme:
  name: void
  palette:
    - scheme: slate
      primary: black
      accent: red
      toggle:
        name: Switch to light mode
    - scheme: default
      primary: white
      accent: red
      toggle:
        name: Switch to dark mode
  void:
    animation: none
    glass: medium
    dot_matrix: true
    border: thin
    {custom}
markdown_extensions:
  - admonition
  - tables
  - toc:
      permalink: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.arithmatex:
      generic: true
plugins:
  - search
  - void
site_dir: {site_dir}
"""


def find_browser():
    platform = sys.platform
    candidates = []
    if platform.startswith("win"):
        for ev in ["PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"]:
            base = os.environ.get(ev, "")
            if base:
                candidates.append(
                    os.path.join(base, "Google", "Chrome", "Application", "chrome.exe")
                )
                candidates.append(
                    os.path.join(base, "Microsoft", "Edge", "Application", "msedge.exe")
                )
    elif platform == "darwin":
        candidates += [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        ]
    else:
        candidates += [
            "google-chrome",
            "google-chrome-stable",
            "chromium-browser",
            "chromium",
            "microsoft-edge",
        ]
    for path in candidates:
        if path and os.path.isfile(path):
            return path
    for name in candidates:
        found = shutil.which(name)
        if found:
            return found
    return None


def build_site(workdir: Path, name: str, custom: str) -> Path:
    site_dir = workdir / f"site_{name}"
    shutil.rmtree(site_dir, ignore_errors=True)
    config = BASE_CONFIG.format(
        custom=custom, site_dir=str(site_dir).replace("\\", "/")
    )
    (workdir / "mkdocs.yml").write_text(config, encoding="utf-8")
    (workdir / "docs" / "index.md").write_text(DEMO_INDEX, encoding="utf-8")
    result = subprocess.run(
        ["mkdocs", "build", "--clean"],
        capture_output=True,
        text=True,
        cwd=str(workdir),
    )
    if result.returncode != 0:
        raise RuntimeError(f"mkdocs build failed for {name}:\n{result.stderr}")
    return site_dir


class _Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002 - silent server
        pass


def capture(site_dir: Path, target: Path, browser_exe: str) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: Playwright is required. Install it with: pip install playwright")
        sys.exit(1)

    handler = lambda *a, **k: _Handler(*a, directory=str(site_dir), **k)  # noqa: E731
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as httpd:
        port = httpd.server_address[1]
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(
                    executable_path=browser_exe,
                    headless=True,
                    args=[
                        "--no-sandbox",
                        "--disable-gpu",
                        "--disable-dev-shm-usage",
                        "--hide-scrollbars",
                    ],
                )
                context = browser.new_context(
                    viewport={"width": 1280, "height": 900},
                    device_scale_factor=1,
                )
                page = context.new_page()
                page.add_init_script(
                    "() => { try { localStorage.setItem('void-color-scheme', 'slate'); } catch (e) {} }"
                )
                page.emulate_media(color_scheme="dark")
                page.goto(f"http://127.0.0.1:{port}/", wait_until="load", timeout=45000)
                time.sleep(1.0)
                page.screenshot(path=str(target), full_page=True)
                browser.close()
        finally:
            httpd.shutdown()


def main() -> None:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--out", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--workdir", type=Path, default=TEMP)
    args = parser.parse_args()

    browser = find_browser()
    if not browser:
        print("Error: No browser found. Install Chrome or Edge.")
        sys.exit(1)
    print(f"Using browser: {Path(browser).name}")

    workdir = args.workdir
    shutil.rmtree(workdir, ignore_errors=True)
    docs_dir = workdir / "docs"
    docs_dir.mkdir(parents=True)
    args.out.mkdir(parents=True, exist_ok=True)

    base_site = build_site(workdir, "base", "")
    (args.out / "components-tmp-on.png").unlink(missing_ok=True)
    capture(base_site, args.out / "components-tmp-on.png", browser)
    print("captured shared 'on' baseline")

    every = [t for t in TOGGLES]
    failed = 0
    for name in every:
        try:
            off_site = build_site(
                workdir, f"off_{name}", f"components:\n      {name}: {{show: false}}"
            )
            (args.out / f"components-{name}-on.png").unlink(missing_ok=True)
            (args.out / f"components-{name}-off.png").unlink(missing_ok=True)
            shutil.copyfile(
                args.out / "components-tmp-on.png",
                args.out / f"components-{name}-on.png",
            )
            capture(off_site, args.out / f"components-{name}-off.png", browser)
            print(f"  [{name}] ok")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  [{name}] FAILED: {exc}")
    (args.out / "components-tmp-on.png").unlink(missing_ok=True)
    print(f"\nGenerated {len(every) - failed}/{len(every)} toggle pairs in {args.out}/")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
