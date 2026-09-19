---
date: 2026-09-19
title: Service Worker & Offline
---

# Service Worker & Caching

## What it is

Void ships a service worker (`sw.js`) that caches static assets and CDN
resources for faster repeat loads and basic offline support. The worker uses
two caches and a versioned-asset bypass strategy so new releases are never
blocked by stale copies.

## When to use it

The service worker is registered automatically on every page. No
configuration is needed — it runs silently in the background. It's especially
valuable on slow connections or for repeat visitors: cached assets load
instantly from the local cache.

## How it works

### Cache names

| Cache | Strategy | What it stores |
|-------|----------|---------------|
| `void-static-v4` | stale-while-revalidate | Same-origin assets: CSS, JS, images, fonts, `void.css`, `void.js` |
| `void-cdn-v4` | cache-first | External: `fonts.googleapis.com`, `fonts.gstatic.com`, `cdnjs.cloudflare.com`, `cdn.jsdelivr.net` |

### Fetch strategy

```
Request
  │
  ├─ Not GET? → pass through
  ├─ Contains /search/? → pass through (MkDocs search worker owns it)
  ├─ External + CDN/font host → cache-first (void-cdn-v4)
  ├─ Same-origin + /assets/ + static extension →
  │    ├─ Has ?v=N → pass through (browser HTTP cache)
  │    └─ No ?v=N → stale-while-revalidate (void-static-v4)
  └─ Everything else → pass through (browser HTTP cache)
```

### Versioned assets

URLs with `?v=N` (the asset versioning scheme) are never served from the
offline cache — they pass through to the browser's HTTP cache, which
revalidates against the server. This is how a new Void release bypasses
stale SW copies immediately.

### Offline behavior

| Scenario | What works |
|----------|-----------|
| Online | Everything — assets served from SW cache on repeat loads |
| Offline, previously visited page | Page may load from browser HTTP cache; assets from `void-static-v4` / `void-cdn-v4` |
| Offline, never visited page | Nothing — HTML pages are not cached by the SW |
| Offline, search | ✗ — the MkDocs search index is not cached by the SW |

### Root-scope cleanup

When the site is mounted at a subpath (e.g. `/docs/`), the SW unregisters any
stale root-scoped (`/`) worker from a previous install to prevent 404 spam.

## Configuration

The service worker requires no configuration. It's registered in
`base.html` on every page:

```javascript
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register(swURL).catch(function () {})
}
```

## Under the hood

- **File:** `void/templates/sw.js` (97 lines)
- **Install:** `skipWaiting()` — new SW activates immediately
- **Activate:** deletes old caches (`void-static-v3`, etc.) and calls
  `clients.claim()` to take over all open tabs
- **Registration:** in `base.html` (line ~762) — runs unconditionally
  (no manifest gate, no feature toggle)
- **Prefetch integration:** `initPrefetch()` issues a low-priority `fetch()`
  only when `navigator.serviceWorker.controller` is set, so the SW cache is
  warmed before navigation

## Accessibility notes

- The SW is invisible to assistive technology — it runs in a background thread.
- Offline behavior is a progressive enhancement: the site works fully online
  and degrades gracefully when the network is unavailable.