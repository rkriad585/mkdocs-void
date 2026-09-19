---
date: 2026-09-19
title: Contributing
---

# Contributing to Void

How to go from "I found a bug" to "my fix is merged."

## Quick start

```bash
git clone https://github.com/rkriad585/mkdocs-void.git
cd mkdocs-void
pip install -e .
npm install
mkdocs serve
```

The site opens at `http://127.0.0.1:8000`.

## Issue labels

| Label | What it means |
|-------|---------------|
| `good first issue` | Small, well-scoped, friendly to a first contributor |
| `help wanted` | Needs a maintainer assist — say "I'll take this" before opening a PR |
| `bug` | Confirmed defect |
| `enhancement` | New feature or improvement |
| `docs` | Documentation-only change |
| `design` | CSS / visual / layout change |
| `chore` | Tooling, CI, non-user-facing |

## First-issue path

1. Find an issue labeled [`good first issue`](https://github.com/rkriad585/mkdocs-void/labels/good%20first%20issue).
2. Comment "I'll take this" so nobody collides.
3. Fork, create a branch (`fix/your-fix`), make the change.
4. Run the checks below, then open a PR.

## Development workflow

```bash
# Build CSS
npm run build

# Watch mode (rebuilds on SCSS changes)
npm run start

# Dev mode (expanded CSS + source maps)
npm run dev

# Serve docs
mkdocs serve

# Lint Python
ruff check void/
```

## PR checklist

Before opening a pull request, confirm:

- [ ] `mkdocs build --clean` succeeds without warnings
- [ ] `npm run build` produces `void.css` without errors
- [ ] `npm test` passes (all smoke checks green)
- [ ] `python tools/check_docs.py` passes all 8 checks
- [ ] You've tested in both dark and light modes
- [ ] You've tested on a mobile viewport (responsive check)
- [ ] You've tested keyboard navigation for any interactive element you changed
- [ ] Documentation is updated if you added or changed a feature
- [ ] `tools/emit_config_reference.py` is run after plugin config changes
- [ ] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `perf:`)

## Commit conventions

The commit prefix drives the [auto-generated changelog](https://github.com/rkriad585/mkdocs-void/blob/main/CHANGELOG.md) (`tools/emit_changelog.py`), so it's part of the feature — not a nicety.

| Prefix | Use for |
|--------|---------|
| `feat:` | New user-facing feature or config surface |
| `fix:` | Bug fix |
| `docs:` | Documentation-only changes |
| `chore:` | Tooling, CI, non-user-facing |
| `refactor:` | Code restructuring without behavior change |
| `perf:` | Performance improvement |

## Code style

- **CSS:** BEM naming with `void-` prefix. No utility frameworks.
- **JavaScript:** Vanilla ES6+, IIFE-wrapped, no dependencies. Uses `$()` and `$$()` helpers.
- **HTML:** Jinja2 templates. Follow MkDocs template conventions.
- **Python:** Standard MkDocs plugin pattern. Use `ruff` for linting.

## Rules

1. **Never delete HTML/Jinja/CSS/classes the theme renders.** Extend or hide via config — never strip.
2. **Never remove a documented feature.** Enabling/disabling goes through config defaults.
3. **Never rename or delete a JS/Python function.** New code may wrap or extend; existing call sites stay intact.
4. **No typos.** Verify every identifier against the source before and after editing.
5. **Don't touch code outside your change's scope.** If a change needs an out-of-scope file, note it in the PR.

## Documentation PRs

- Screenshots are required for any visual change (use `tools/screenshots_gen.py`).
- Never link or embed any PLAN file (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`) from docs.
- Run `tools/check_docs.py` before committing — it catches broken links, missing H1s, stale config keys, and template violations.

## Reporting issues

Use the [GitHub issue tracker](https://github.com/rkriad585/mkdocs-void/issues) to report bugs or request features. Include:

- MkDocs version (`mkdocs --version`)
- Python version (`python --version`)
- Browser and OS
- Steps to reproduce
- Expected vs actual behavior

## Contributing to the Wiki

The [GitHub wiki](https://github.com/rkriad585/mkdocs-void/wiki) is a
community-editable companion to these docs.

- **Quick edits:** click **Edit** on any wiki page directly on GitHub.
- **Permanent changes:** edit files in `tools/wiki_sync/` via a PR — the
  `wiki-sync.yml` Action pushes them on the next release.
- **Rules:** no PLAN files; every page links back to the canonical docs;
  direct wiki edits may be overwritten by the next sync.

See [Contributing to the Wiki](https://github.com/rkriad585/mkdocs-void/wiki/Contributing-to-the-Wiki) for details.

## Community

- [Discussions](https://github.com/rkriad585/mkdocs-void/discussions) — questions, showsites, ideas
- [GitHub Sponsors](https://github.com/sponsors/rkriad585) — fund development

---

[Back to README](index.md)