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
`extra.void_logo_light` → `extra.void_logo_dark` → `theme.logo` →
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

## Under the hood

- **File:** `void/plugins/void_plugin.py` — `_pwa_manifest()` (line ~2749),
  `_pwa_icon()` (line ~2778), auto-generated at `on_post_build()` (line ~3026)
- **Defaults:** `_VOID_DEFAULT_PWA` (line ~832) — `manifest: True`,
  `display: "standalone"`, `icons: True`, `background_color: "#111114"`
- **Validation:** `_validate_pwa()` (line ~1692) rejects invalid `display`
  values and non-boolean `manifest`/`icons`
- **Custom manifest:** `extra.void_manifest` overrides the auto-generated one
  — set it to an external URL or a local path to use your own manifest

## Accessibility notes

- The `display: "standalone"` mode removes browser chrome; ensure your
  navigation and reading experience works without the address bar.
- `background_color` and `theme_color` affect the splash screen and system
  UI — pick colors that meet contrast ratios for the loading state.