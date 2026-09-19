---
date: 2026-09-19
title: SPA Navigation
---

# SPA Navigation & Scroll Restore

## What it is

Void intercepts link clicks and fetches the target page as HTML, swapping
only the article, TOC, sidebar, and header — without a full page reload.
Scroll position is saved per page and restored on return, and the browser
back/forward buttons work correctly.

## When to use it

SPA navigation is always on. It makes the docs feel instant: clicking a link
in the sidebar or article swaps content in ~100ms instead of a full page
load. The prefetch layer pre-fetches links on hover so the swap is often
instantaneous.

## How it works

### Click interception

A document-level click listener checks every `<a>` click:

1. Is it a same-site, `http(s)` link with `target="_self"` (or no target)?
2. Is it not a `mailto:`, `tel:`, or hash-only link?
3. Is it under the configured `base` path?

If all pass, `navigateTo(url, true)` runs instead of a full navigation.

### Page swap

`navigateTo()` does:

1. Saves the current scroll position to `void-scroll-pos`.
2. Pushes a new history entry.
3. Fetches the target page with `X-Void-SPA: 1` header.
4. Parses the response and extracts `.void-article`, `.void-toc`,
   `.void-nav`, `.void-footer`, and the header page-title.
5. Swaps them into the DOM via `applyPage()`.
6. Re-runs 19 page-scoped initializers (`reinitPageScoped()`).
7. Restores scroll position (top for new pages; saved position for back/forward).
8. Closes any open overlays (sidebar, TOC, search).

### Prefetch on hover

When `components.prefetch.show` is true (default), hovering a link triggers
a `<link rel="prefetch">` for the target page. If the service worker is
active, a low-priority `fetch()` is also issued to warm the SW cache.

Prefetch is skipped when:

- `navigator.connection.saveData` is true
- The link is cross-origin and `prefetch.external` is false (default)
- The URL contains `/#`
- The URL matches any `prefetch.exclude` substring

### Scroll restore

Scroll positions are stored in `void-scroll-pos` as a map of
`pageURL → { y, x, at }`. On back/forward, the saved position is restored.
At boot, if the site opens at the root and the last visit was a different
page, `_voidRestoreScroll` navigates to it with `{ resume: true }`.

## Configuration

```yaml
theme:
  void:
    components:
      prefetch:
        show: true                      # Enable prefetch-on-hover (default true)
        external: false                 # Also prefetch off-site links (default false)
        exclude: []                     # URL substrings to never prefetch
```

## Under the hood

- **File:** `void.js` — `initSPANavigation(config)` (line ~5117),
  `navigateTo(url, pushState)` (line ~5311), `extract(html)` (line ~5146),
  `applyPage(data)` (line ~5163), `reinitPageScoped()` (line ~5197)
- **Scroll restore:** `void-scroll-pos` — `pageKey → { y, x, at }` map,
  written directly to `localStorage` (not via the `void-` prefix helpers).
- **Session:** `void-session.lastPage` / `void-session.lastAt` — last visited
  page, used for resume-to-last-page on boot.
- **Prefetch:** `initPrefetch(config)` (line ~5467) — gated by
  `components.prefetch.show`; uses `<link rel="prefetch">` and optional
  low-priority `fetch()`.
- **Safety:** cross-origin, `mailto:`, `tel:`, `download` attr, `target !== "_self"`,
  and `#`-only links are never intercepted.

## Accessibility notes

- SPA swaps preserve the document title and ARIA live regions, so screen
  readers announce the new page.
- Focus is not moved after a swap — the user stays at the link they clicked.
- The back/forward buttons work correctly via `popstate`, and scroll position
  is restored, so keyboard navigation is uninterrupted.