---
date: 2026-09-19
title: Testing & Harnesses
---

# Testing & Harnesses

What each test covers, how to run them, and how to add your own.

## Test suites

Void has three verification layers that run in CI and locally:

| Layer | Command | What it checks |
|-------|---------|---------------|
| JS smoke tests | `npm test` | 55 checks: boot sequence, localStorage, search, lightbox, feedback, announcement, consent, giscus, repo popover, i18n, prefetch, link rebase, asset modes |
| Doc lint | `python tools/check_docs.py` | 8 checks: PLAN links, intra-doc links, screenshots, config keys, H1/ markers, nav sync, component template, design tokens |
| Strict build | `mkdocs build --strict` | Zero warnings — catches template errors, missing pages, broken refs |

All three must pass before opening a PR.

## JS smoke tests (`npm test`)

**File:** `tests/void.test.js` (1412 lines)

The test stubs a minimal DOM/browser environment and loads the theme's `void.js` IIFE to verify the boot sequence runs without throwing. It then exercises specific features.

### What each check covers

| # | Check | What it verifies |
|---|-------|-----------------|
| 1 | IIFE boot completes without throwing | `void.js` loads and all `init*` functions run with a null config |
| 2 | Expired note purged after TTL | A 1-year-old note in `void-notes` is removed on boot |
| 3 | Fresh note retained after TTL purge | A fresh note survives the purge |
| 4 | `?q=` deep link auto-opens search | Query param opens the search overlay with the query pre-filled |
| 5 | Copy link writes correct deep-link URL | Share button writes `?q=` URL without `#fragment` |
| 6 | `result.show_share: false` hides share button | Config disables the per-result share button |
| 7 | Image lightbox opens on click | Clicking an image creates a `.void-zoom` overlay |
| 7b | Lightbox disabled via config | `content.typography.image_lightbox: false` prevents overlay creation |
| 8 | Lightbox nav, zoom, copy, close | Arrow keys navigate, zoom scales, copy falls back to URL, close works after navigation |
| 9 | Feedback widget renders | `.void-feedback` appears under the article when `repo_url` is set |
| 10 | Feedback Yes opens prefilled issue URL | Click creates `/issues/new?labels=...&title=...&body=...` |
| 11 | Feedback hidden when disabled | `enabled: false` suppresses the widget |
| 12 | Announcement bar renders | `.void-announcement` appears when `text` is set |
| 13 | Announcement dismiss persists + removes bar | Click writes `void-announcement-dismissed-<text>: "1"` and removes the bar |
| 14 | Already-dismissed announcement not re-rendered | Stored key prevents re-render on next boot |
| 15 | Floating position variants (top/center) | `position: "top"` renders without backdrop; `"center"` renders with backdrop |
| 16 | Closing centered announcement removes backdrop | Backdrop count decreases by 1 |
| 17 | Consent absent when no integration | `consent_needed: false` → no `.void-consent` |
| 18 | Consent renders when integration configured | `.void-consent` with accept button appears |
| 19 | Accept persists consent flag | `void-consent: "accepted"` written to localStorage |
| 20 | Decline persists consent flag | `void-consent: "declined"` written to localStorage |
| 21 | Giscus loader injected on configured repo | `<script data-giscus>` added to `<head>` with correct attrs |
| 22 | Giscus defers behind consent | Script not injected before consent is accepted |
| 23 | Giscus loads after consent | Script injected after clicking accept |
| 24 | Repo popover boots with hooks + bindings | `_voidRepoShow`/`_voidRepoHide` exist, hover/focus/escape bindings wired |
| 25 | Repo popover dismissible (no auto-close) | Escape + click-outside close; no timer |
| 26 | Repo popover open/stay/close behavior | Opens on hover, stays on inside press, closes on outside press |
| 27 | Repo popover shows all fields by default | Every info section rendered when no `fields` filter |
| 28 | Repo popover `fields` filter narrows output | `["stars","forks"]` hides other sections |
| 29 | Repo popover disabled via config | `show: false` suppresses hooks |
| 30 | i18n overrides translate repo popover labels | `translations.repo.author` replaces "Author" |
| 31 | Dark-aware images follow boot scheme | `data-md-scheme-dark`/`data-md-scheme-light` src swap |
| 32 | Dev preview rewrites production URLs to localhost | Link rebase in dev mode |
| 33 | Deployed origin leaves links untouched | No rebase on production |
| 34 | No site_url leaves links untouched | Fallback behavior |
| 35 | Prefetch appends `<link rel=prefetch>` on hover | Internal link prefetch on pointerover |
| 36 | Hovering same link twice doesn't duplicate | Dedup check |
| 37 | Off-site link not prefetched when `external: false` | Cross-origin skip |
| 38 | Off-site link IS prefetched when `external: true` | Cross-origin prefetch enabled |
| 39 | Prefetch disabled when `show: false` | Component gate |
| 40 | Asset URL resolves in local + bundle modes | `assetUrl()` works with `assets.mode` |
| 41 | Standalone config builder ships in `docs/assets/` | File exists and is >1000 bytes |
| 42–45 | Builder carries markers, is dependency-free | Structural checks on `config-builder.html` |
| 46–49 | Builder TOC trigger + cluster integration | Enabled/disabled states, gear action dispatch |

### How to run

```bash
npm test
```

Output ends with `All JS smoke checks passed (55 checks).` or reports failures with line numbers.

### How to add a test

1. Find the right insertion point (tests are numbered sequentially).
2. Use `bootIIFE()` to boot `void.js` with your config fixture:

```javascript
const myBoot = bootIIFE({
  location: { origin: "https://x", pathname: "/page/", search: "", href: "https://x/page/", hash: "" },
  config: {
    base: "/",
    components: { /* your component config */ },
    content: {},
    void_search: { enabled: false },
    translations: {},
  },
  searchDom: null,
  stored: {},   // pre-populate localStorage keys here
})
```

3. Assert with `check("description", booleanCondition)`.

**Fixture helpers:**

| Helper | Purpose |
|--------|---------|
| `makeNode()` | Creates a stub DOM element with `classList`, `setAttribute`, `addEventListener`, etc. |
| `searchDomFixture()` | Returns `{ checkbox, searchEl, input, status, list, closeBtn }` for search tests |
| `zoomImageFixture()` | Returns a stub `<img>` for lightbox tests |
| `repoPopoverFixture()` | Returns `{ wrap, link, pop }` for repo popover tests |
| `engagementBaseConfig(extra)` | Returns a full config base for feedback/announcement/consent tests |
| `findClass(root, token)` | Depth-first search for a descendant by className token |

**Pre-populating localStorage:**

```javascript
const myBoot = bootIIFE({
  stored: { "void-notes": JSON.stringify([{ id: "x", url: "/", ts: Date.now() }]) },
  // ...
})
```

**Accessing the search Worker shim:**

The Worker shim in the test harness fires results when `msg.query` is sent. The results are rendered into `_searchDom.list._children` as row nodes.

## Doc lint (`tools/check_docs.py`)

**File:** `tools/check_docs.py`

| # | Check | What it catches |
|---|-------|-----------------|
| 1 | PLAN-file links | Docs linking to `PLAN.md`, `WHY_PLAN.md`, etc. |
| 2 | Intra-doc links | Broken relative links between doc pages |
| 3 | Screenshot contract | Pages in `docs/components/` must have matching screenshots |
| 4 | Config keys | YAML keys used in docs must exist in the plugin's token map |
| 5 | H1 + no leftover markers | Every page has exactly one H1; no leftover markers |
| 6 | Nav sync | Every file in `docs/` is in `mkdocs.yml` nav; every nav entry has a file |
| 7 | Component 7-section template | Component pages follow the required section structure |
| 8 | Design tokens match SCSS | CSS custom properties documented in design pages match the SCSS source |

### How to run

```bash
python tools/check_docs.py
```

All 8 checks print `[ ok ]`. Failures print `[FAIL]` with the file and reason.

### How to add a check

1. Open `tools/check_docs.py`.
2. Add a new function following the pattern of existing checks.
3. Register it in the `checks` list at the bottom.
4. The check runs against all files in `docs/` and `mkdocs.yml`.

## Strict build

```bash
mkdocs build --strict --clean
```

Zero warnings means the build is clean. Any warning is treated as an error.

## CI workflows

| Workflow | Trigger | What it does |
|----------|---------|-------------|
| `docs.yml` | Push to `main` | Builds docs, runs `check_docs.py`, deploys to GitHub Pages |
| `compat.yml` | Push to `main` (void/**) | Tests against MkDocs 1.5.3, 1.6.1, 2.0.dev0 |
| `integrations.yml` | Push to `main` | Tests third-party plugin compatibility |
| `benchmarks.yml` | Push to `main` | Runs page-weight benchmarks |
| `changelog.yml` | Push to `main` | Generates changelog PR from conventional commits |
| `release.yml` | Tag push | Publishes to PyPI |

## Recipes

### Adding a new init function to void.js

1. Write the function in `void.js`.
2. Call it from the boot sequence (the IIFE at the bottom).
3. Add a smoke test that boots with the relevant config and asserts the function ran.
4. Run `npm test` to confirm.

### Adding a new config key

1. Add the key to `_VOID_DEFAULT_*` in `void/plugins/void_plugin.py`.
2. Add it to `_VOID_TOKEN_MAP` for the doc lint check.
3. Run `python tools/emit_config_reference.py` to regenerate the reference page.
4. Document the key in the relevant docs page.
5. Run `python tools/check_docs.py` to confirm the key is recognized.

---

[Back to README](index.md)