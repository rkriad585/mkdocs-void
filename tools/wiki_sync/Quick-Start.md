# Quick Start

## Install

```bash
pip install mkdocs-void
```

## Scaffold a project

```bash
void new my-docs
cd my-docs
```

## Serve

```bash
mkdocs serve
```

Open `http://127.0.0.1:8000`.

## Key features

- Press `/` to open search
- Press `?` for keyboard shortcuts
- Press `Ctrl+Shift+N` for notes panel
- Press `Alt+Shift+R` for reading mode
- Press `Alt+Shift+A` for action cluster

## Deploy

```yaml
# .github/workflows/docs.yml
name: Deploy docs
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install mkdocs-void
      - run: mkdocs build --strict
      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

Full docs: [https://rkriad585.github.io/mkdocs-void/](https://rkriad585.github.io/mkdocs-void/)