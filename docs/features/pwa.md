---
date: 2026-09-19
title: PWA Manifest
---

# PWA Manifest

## What it is

Void auto-generates a `manifest.webmanifest` at build time so the docs site
is installable as a Progressive Web App. The manifest provides the app name,
icons, theme color, display mode, and start URL — everything a browser needs
to offer the "Add to Home Screen" prompt.

## When to use it

The manifest is on by default. It makes the docs installable on mobile
devices and desktop browsers that support PWA installation. The service
worker (`sw.js`) is already registered, so the installed app works offline
for previously visited pages and cached assets.

## How it works

### Manifest generation

The plugin builds the manifest from `theme.void.pwa` merged with site-level
fallbacks:

```yaml
extra:
  void_theme_color: "#ff3030"    # fallback for pwa.theme_color
  site_url: "https://example.com" # fallback for pwa.start_url
```

```yaml
theme:
  void:
    pwa:
      manifest: true              # Emit manifest.webmanifest (default true)
      display: "standalone"       # "standalone" | "fullscreen" | "minimal-ui" | "browser"
      icons: true                 # Auto-resolve icon from logo/favicon
      theme_color: ""             # Falls back to extra.void_theme_color
      background_color: "#111114" # Splash screen background
      start_url: ""               # Falls back to site_url or "/"
```

The icon is resolved from the same chain as social cards:
`extra.void_logo_light` -> `extra.void_logo_dark` -> `theme.logo` ->
`theme.favicon`. Local files are used as-is; remote logos are fetched at
build time into the site directory.

### Generated manifest

```json
{
  "name": "My Docs",
  "short_name": "My Docs",
  "start_url": "https://example.com/",
  "display": "standalone",
  "background_color": "#111114",
  "theme_color": "#ff3030",
  "icons": [
    {
      "src": "assets/images/logo.svg",
      "sizes": "any",
      "type": "image/svg+xml"
    }
  ]
}
```

### HTML output

When the manifest is active, the plugin also emits:

```html
<link rel="manifest" href="manifest.webmanifest">
<meta name="application-name" content="My Docs">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
```

### Custom manifest

To use your own manifest instead of the auto-generated one:

```yaml
extra:
  void_manifest: "https://example.com/custom-manifest.json"
```

Or place a `manifest.webmanifest` in `docs/` and disable the auto-generated
one:

```yaml
theme:
  void:
    pwa:
      manifest: false
```

## Asset modes

Void can vendor CDN dependencies (highlight.js, Mermaid, KaTeX) for fully
offline-capable builds. This is configured via `theme.void.assets.mode`:

| Mode | Description |
|------|-------------|
| `"cdn"` (default) | Runtime CDN loading. Builds are deterministic, no network needed at build time. |
| `"local"` | Vendors all three libraries into `site/assets/vendor/` at build time. Each component loader points at its own local copy. |
| `"bundle"` | Like `local`, but concatenates all vendored JS into a single file (`assets/vendor/bundle/void-offline.js`). |

```yaml
theme:
  void:
    assets:
      mode: "local"                # "cdn" | "local" | "bundle"
      vendor_dir: "assets/vendor"  # Where vendored files go (default)
      timeout: 20                  # Download timeout in seconds (default 20)
```

!!! note
    Google Fonts stay external in every mode. `inline_critical_css` only
    applies with `local`/`bundle` and is ignored with a warning under `cdn`.

### Vendored libraries

| Library | CDN URL | Version |
|---------|---------|---------|
| highlight.js | `cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js` | 11.9.0 |
| highlight.js CSS | `cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/` | 11.9.0 |
| Mermaid.js | `cdn.jsdelivr.net/npm/mermaid@10.9.8/dist/mermaid.min.js` | 10.9.8 |
| KaTeX JS | `cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js` | 0.16.9 |
| KaTeX CSS | `cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css` | 0.16.9 |

In `local` mode, each file is downloaded separately. In `bundle` mode, all
JS is concatenated into `bundle/void-offline.js`. Failed downloads fall back
to CDN URLs.

## Service worker caching

The `sw.js` service worker caches assets for faster repeat loads and basic
offline support:

| Cache | Strategy | What it stores |
|-------|----------|---------------|
| `void-static-v4` | stale-while-revalidate | Same-origin assets (CSS, JS, images, fonts) |
| `void-cdn-v4` | cache-first | External CDN fonts (Google Fonts, cdnjs, jsdelivr) |

URLs with `?v=N` (asset versioning) pass through to the browser HTTP cache,
so new releases bypass stale SW copies immediately.

### Offline behavior

| Scenario | What works |
|----------|-----------|
| Online | Everything |
| Offline, previously visited page | Assets from SW cache; page may load from browser cache |
| Offline, never visited page | Nothing (HTML pages are not cached) |
| Offline, search | No (search index is not cached) |

### Full offline with asset vendoring

For fully offline-capable docs:

```yaml
theme:
  void:
    assets:
      mode: "local"    # or "bundle"
    pwa:
      manifest: true
```

This vendors all CDN libraries and generates the PWA manifest. The only
limitation is that HTML pages themselves are not cached by the SW — they
depend on the browser HTTP cache.

## How to test

### Install prompt

1. Build and serve: `mkdocs serve`
2. Open Chrome DevTools > Application > Manifest
3. Verify the manifest loads and all fields are correct
4. On mobile: the "Add to Home Screen" prompt appears after a few visits

### Offline

1. Build with `assets.mode: "local"` or `"bundle"`
2. Serve with `mkdocs serve`
3. Open DevTools > Application > Service Workers — verify the SW is active
4. Go offline (DevTools > Network > Offline)
5. Reload the page — assets load from cache
6. Navigate to a previously visited page — it may load from browser cache

### Audit

```bash
npx lighthouse http://127.0.0.1:8000 --view
```

Check the PWA section for installability and offline criteria.

## Under the hood

- **File:** `void/plugins/void_plugin.py` — `_pwa_manifest()` (line ~2749),
  `_pwa_icon()` (line ~2778), auto-generated at `on_post_build()` (line ~3026)
- **Defaults:** `_VOID_DEFAULT_PWA` (line ~832) — `manifest: True`,
  `display: "standalone"`, `icons: True`, `background_color: "#111114"`
- **Validation:** `_validate_pwa()` (line ~1692) rejects invalid `display`
  values and non-boolean `manifest`/`icons`
- **Assets:** `_VOID_DEFAULT_ASSETS` (line ~853) — `mode: "cdn"`,
  `vendor_dir: "assets/vendor"`, `timeout: 20`
- **Asset modes:** `_VOID_ASSET_MODES` (line ~852) — `frozenset({"cdn", "local", "bundle"})`
- **Vendoring:** `on_config()` (line ~2163) rewrites CDN URLs when mode is
  `local` or `bundle`; downloads happen in `on_files()` (line ~2502)

## Accessibility notes

- The `display: "standalone"` mode removes browser chrome; ensure your
  navigation and reading experience works without the address bar.
- `background_color` and `theme_color` affect the splash screen and system
  UI — pick colors that meet contrast ratios for the loading state.
- The SW is invisible to assistive technology — it runs in a background thread.