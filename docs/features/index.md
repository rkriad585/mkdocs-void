---
date: 2026-09-19
---

# Features & Behavior

## What it is

Void isn't a static theme — it's an interactive documentation app that
happens to build as plain HTML. This section documents every behavior:
keyboard shortcuts, overlays, navigation, persistence, offline support, and
how the theme degrades gracefully when JavaScript is unavailable.

## How it works

All features are driven by `void.js` (≈5,500 lines), the theme's
single-file JavaScript runtime. Every behavior is registered through an
`init*()` function and called once at boot, then re-run after each SPA
swap. Configuration is injected into a `<script id="__config">` block at
build time, and all feature states are persisted in `localStorage` under
the `void-` prefix.

## Features

### Navigation & search

- [Search](search.md) — full-screen modal, `/` shortcut, suggestions, context snippets, highlighting, copy-link per result.
- [SPA navigation & scroll restore](spa-navigation.md) — prefetch-on-hover, client-side page swaps, scroll position memory, resume-to-last-page.

### Productivity overlays

- [Reading mode](reading-mode.md) — `Alt+Shift+R` distraction-free reading view that hides chrome and widens the article.
- [Action cluster](action-cluster.md) — `Alt+Shift+A` floating action button that expands into quick-access shortcuts.
- [Focus timer](focus-timer.md) — `Alt+Shift+T` Pomodoro-style countdown with TOC widget and reading chip.
- [Notes panel](notes-panel.md) — `Ctrl+Shift+N` sticky notes with export, TTL, and cross-page persistence.
- [Keyboard reference](keyboard.md) — `?` modal listing every binding, built dynamically from config.

### Chrome behavior

- [Reading progress](reading-progress.md) — progress bar at the top of the article.
- [Back-to-top](back-to-top.md) — floating button that appears after scrolling.
- [TOC scrollspy](toc-scrollspy.md) — active-heading highlight in the "On this page" rail.

### Offline & PWA

- [Service worker & caching](service-worker.md) — `sw.js` strategy diagram, cache names, versioned assets.
- [PWA manifest](pwa.md) — `manifest.webmanifest` auto-generation, installability, icons.

### Persistence & external data

- [Persistence](persistence.md) — every `localStorage` key the theme reads and writes.
- [Repo popover](repo-popover.md) — `Ctrl+Shift+G` GitHub project card with 1-hour cache.

## Graceful degradation

The table below shows what still works when JavaScript is disabled, when the
device is offline, when `prefers-reduced-motion: reduce` is active, or when
the browser lacks `backdrop-filter` support.

| Feature | No JS | Offline (previously visited) | Reduced motion | No backdrop-filter |
|---------|-------|------------------------------|----------------|-------------------|
| Search | ✗ — no worker, no modal | ✗ — search index not cached by SW | — | — |
| SPA navigation | ✗ — full page reloads | ✓ — browser cache serves pages | — | — |
| Prefetch | ✗ — no hover prefetch | ✓ — pages may be in browser cache | — | — |
| Reading mode | ✗ — no JS toggle | ✓ — CSS-only hiding when persisted | — | — |
| Action cluster | ✗ — no JS rendering | ✓ — rendered by server on first load | — | — |
| Focus timer | ✗ — no JS countdown | ✗ — timer state in localStorage | — | — |
| Notes panel | ✗ — no JS overlay | ✓ — panel rendered on first load | — | — |
| Keyboard shortcuts | ✗ — no key handling | ✓ — help modal rendered on first load | — | — |
| Reading progress | ✗ — no scroll handler | ✓ — bar rendered, stays at 0% | — | — |
| Back-to-top | ✗ — no scroll handler | ✓ — button stays hidden | — | — |
| TOC scrollspy | ✗ — no scroll handler | ✓ — no active highlight | — | — |
| Glass morphism | — | — | — | ✓ — falls back to flat semi-transparent fill |
| Animations (page, toast, stagger) | — | — | ✓ — CSS `prefers-reduced-motion: reduce` disables transitions and keyframes | — |
| Palette toggle | ✓ — server-rendered scheme; no runtime toggle | ✓ — scheme stored in localStorage | — | — |
| Tabs | ✓ — `<input type="radio">` fallback renders all panels | ✓ | — | — |
| Task lists | ✓ — native checkboxes still function | ✓ — state in localStorage | — | — |
| Admonitions (collapsible) | ✓ — native `<details>` toggles work | ✓ | — | — |
| Lightbox | ✗ — no JS overlay | ✓ | — | — |
| Toast | ✗ — no JS notification | ✓ — toast element hidden | — | — |
| Repo popover | ✗ — no JS fetch | ✗ — API data not cached by SW | — | — |
| Service worker | — | ✓ — assets served from `void-static-v4` / `void-cdn-v4` caches | — | — |
| PWA install | — | ✓ — manifest + SW already registered | — | — |
| Cookie consent | ✓ — banner rendered server-side | ✓ — state in localStorage | — | — |

**Legend:** ✓ = fully functional; ✗ = not functional; — = not applicable (feature doesn't depend on that condition).

## Configuration

Features are toggled under `theme.void.components` and `theme.void.*`:

```yaml
theme:
  void:
    components:
      search:
        show: true
      notes:
        show: true
      keyboard_help:
        show: true
      prefetch:
        show: true
        external: false
        exclude: []
      repo_popover:
        show: true
      toast:
        show: true
```

## Under the hood

- `void.js` boots via `initTheme()` → `initSearch()` → `initSPANavigation()`
  → `initPrefetch()` → `initScrollBehavior()` → `initBackToTop()` →
  `initTocTracking()` → and the remaining `init*()` functions. Each is
  idempotent and re-runs after SPA swaps via `reinitPageScoped()`.
- Configuration lives in `window.__config` (parsed from the `#__config`
  `<script>` tag); the plugin injects `theme.void.*` as a flat JSON object
  at build time.
- All persistence uses `localStorage` under the `void-` prefix (e.g.
  `void-color-scheme`, `void-notes`, `void-scroll-pos`).

## Accessibility notes

- Every overlay (search, notes, help, timer settings) traps focus and can
  be closed with `Esc`.
- Keyboard shortcuts are configurable and can be remapped or disabled
  individually under `theme.void.keyboard.shortcuts`.
- Reading mode and the focus timer honor `prefers-reduced-motion` and can
  be disabled per-feature via config.
- The action cluster renders with `aria-label` on each button and
  `role="group"` on the menu.