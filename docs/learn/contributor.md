---
date: 2026-09-19
title: "Level 4 — Contributor"
---

# Level 4 — Contributor

**Time:** ongoing

You'll understand the architecture, run the full test suite, and make your
first contribution.

## What you'll learn

- How the codebase is organized
- How to run the development environment
- How the test harnesses work
- How to make and verify a change
- How to open a PR

## Prerequisites

- Completed [Level 3 — Customizer](customizer.md)
- Git installed
- GitHub account

## Step 1 — Fork and clone

```bash
# Fork on GitHub, then:
git clone https://github.com/your-username/mkdocs-void.git
cd mkdocs-void
pip install -e .
npm install
```

## Step 2 — Understand the architecture

Read [Architecture](../architecture.md) for the full picture. The key files:

| File | What it does |
|------|-------------|
| `void/plugins/void_plugin.py` | MkDocs plugin — config defaults, hooks, SW generation |
| `void/templates/base.html` | Root HTML template |
| `void/templates/assets/javascripts/void.js` | All client-side behavior (5500+ lines) |
| `void/templates/assets/stylesheets/` | SCSS source (tokens + components) |
| `tools/build.js` | SCSS → CSS build pipeline |
| `tools/check_docs.py` | Doc lint (8 checks) |
| `tests/void.test.js` | JS smoke tests (55 checks) |

## Step 3 — Run the dev environment

```bash
# Terminal 1: watch CSS
npm run start

# Terminal 2: serve docs
mkdocs serve
```

Edit SCSS in `void/templates/assets/stylesheets/` — changes rebuild
automatically. Edit `void.js` — reload the browser.

## Step 4 — Run the full test suite

```bash
# JS smoke tests
npm test

# Doc lint
python tools/check_docs.py

# Strict build
mkdocs build --strict --clean
```

All three must pass before opening a PR.

## Step 5 — Make a change

Pick a [`good first issue`](https://github.com/rkriad585/mkdocs-void/labels/good%20first%20issue) or
create a small improvement:

1. Create a branch:

   ```bash
   git checkout -b fix/your-fix
   ```

2. Make your change.

3. Run the checks:

   ```bash
   npm test
   python tools/check_docs.py
   mkdocs build --strict --clean
   ```

4. If you changed plugin config, regenerate the reference:

   ```bash
   python tools/emit_config_reference.py
   ```

5. Commit with a [Conventional Commit](https://www.conventionalcommits.org/) prefix:

   ```bash
   git commit -m "fix: correct search result highlighting"
   ```

## Step 6 — Open a PR

1. Push your branch:

   ```bash
   git push origin fix/your-fix
   ```

2. Open a pull request against `main`.

3. Fill in the PR template:

   - What changed and why
   - Screenshot for visual changes
   - Checklist: `mkdocs build --clean`, `npm test`, `check_docs.py` all pass

4. Wait for CI to go green.

## Testing recipes

### Adding a new init function

1. Write the function in `void.js`.
2. Call it from the boot IIFE.
3. Add a smoke test in `tests/void.test.js`:

   ```javascript
   const myBoot = bootIIFE({
     location: { origin: "https://x", pathname: "/page/", search: "", href: "https://x/page/", hash: "" },
     config: { base: "/", components: {}, content: {}, void_search: { enabled: false }, translations: {} },
     searchDom: null,
     stored: {},
   })
   check("my feature boots without throwing", myBoot)
   ```

4. Run `npm test`.

### Adding a new config key

1. Add the default in `void/plugins/void_plugin.py` (`_VOID_DEFAULT_*`).
2. Add the key to `_VOID_TOKEN_MAP`.
3. Run `python tools/emit_config_reference.py`.
4. Document the key in the relevant docs page.
5. Run `python tools/check_docs.py`.

### Adding a new doc page

1. Create the `.md` file in `docs/`.
2. Add the nav entry in `mkdocs.yml`.
3. Run `python tools/check_docs.py` — the nav sync check confirms it's wired.

## Verify you got it

- [ ] Forked and cloned the repo
- [ ] `npm test` passes (55/55)
- [ ] `python tools/check_docs.py` passes (8/8)
- [ ] `mkdocs build --strict` builds clean
- [ ] Made a change and verified it locally
- [ ] Opened a PR with a Conventional Commit title
- [ ] CI is green

---

[Back to Learn](index.md)