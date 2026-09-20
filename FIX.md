# FIX.md — Search URL Routing, Caching & Comprehensive Bug Fixes

**Date:** 2026-09-20
**Status:** READY TO EXECUTE
**Scope:** 3 categories, 12 fixes, 5 files

---

## Problem 1: Search URLs Missing Base Path

**Symptom:** Search results redirect to `https://rkriad585.github.io/components/toast/` instead of `https://rkriad585.github.io/mkdocs-void/components/toast/`

**Root Cause:** `config.base` is captured once at boot in `initSearch()` and never updated after SPA navigation. After the user navigates via SPA, `config.base` is stale, producing wrong relative URLs.

### Fix 1.1 — Use `config.site_url` for search result href construction
**File:** `void/templates/assets/javascripts/void.js`
**Lines:** ~541, ~670

```js
// BEFORE (line ~541):
const base = (config && config.base) || "."

// AFTER:
const siteUrl = (config && config.site_url) || ""
```

Then at line ~670:
```js
// BEFORE:
const href = joinUrl(base, doc.location || "")

// AFTER — build absolute URL from site_url:
const href = siteUrl
  ? siteUrl.replace(/\/+$/, "") + "/" + (doc.location || "")
  : (doc.location || "")
```

This ensures search result links are always absolute and include the full project path, regardless of SPA state.

---

## Problem 2: Caching & Slow Loading

### Fix 2.1 — Add precache manifest to SW install handler
**File:** `void/templates/sw.js`
**Lines:** 12–14

```js
// BEFORE:
self.addEventListener("install", function (e) {
  e.waitUntil(self.skipWaiting())
})

// AFTER:
self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(CACHE_STATIC).then(function (cache) {
      return cache.addAll([
        "./assets/void.css",
        "./assets/javascripts/void.js"
      ])
    }).then(function () { return self.skipWaiting() })
  )
})
```

### Fix 2.2 — Add GitHub hosts to SW CDN allowlist
**File:** `void/templates/sw.js`
**Lines:** 53–58

```js
// BEFORE:
function isCDNOrFont(host) {
  return host === "fonts.googleapis.com" ||
         host === "fonts.gstatic.com" ||
         host === "cdnjs.cloudflare.com" ||
         host === "cdn.jsdelivr.net"
}

// AFTER:
function isCDNOrFont(host) {
  return host === "fonts.googleapis.com" ||
         host === "fonts.gstatic.com" ||
         host === "cdnjs.cloudflare.com" ||
         host === "cdn.jsdelivr.net" ||
         host === "api.github.com" ||
         host === "avatars.githubusercontent.com" ||
         host === "github.com"
}
```

### Fix 2.3 — Add lazy loading + priority hints to avatar `<img>`
**File:** `void/templates/assets/javascripts/void.js`
**Lines:** ~5006–5007

```js
// BEFORE:
avatarHtml = '<img class="void-repo-pop__avatar" src="' + repoPopoverEscape(avatarSrc)
  + '" alt="' + repoPopoverEscape(ownerName || ownerLogin) + '" referrerpolicy="no-referrer">'

// AFTER:
avatarHtml = '<img class="void-repo-pop__avatar" src="' + repoPopoverEscape(avatarSrc)
  + '" alt="' + repoPopoverEscape(ownerName || ownerLogin)
  + '" referrerpolicy="no-referrer" loading="lazy" decoding="async" fetchpriority="low">'
```

### Fix 2.4 — Batch API calls: render repo+owner first, tags+commits after
**File:** `void/templates/assets/javascripts/void.js`
**Lines:** ~4913–4935

Split the `Promise.all` into two phases:
1. **Phase 1 (immediate):** `fetch(api)` + `fetch(USER_API_BASE + owner)` → render popover with name, description, stars, forks, avatar
2. **Phase 2 (background):** `fetch(api + "/tags?per_page=1")` + `fetch(api + "/commits?per_page=1")` → patch tags/commits rows after render

This makes the popover appear instantly with core data, while tags and commits fill in 100–200ms later.

---

## Problem 3: Comprehensive Bugs

### Fix 3.1 — CRITICAL: SPA click guard logic
**File:** `void/templates/assets/javascripts/void.js`
**Line:** 5417

```js
// BEFORE:
if (e.button !== 0 && e.metaKey && e.ctrlKey) return

// AFTER:
if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey) return
```

**Impact:** This was causing ctrl+click, middle-click, and Cmd+click to trigger SPA navigation instead of opening a new tab, leading to 404 redirects.

### Fix 3.2 — HIGH: Mermaid diagram pan guard logic
**File:** `void/templates/assets/javascripts/void.js`
**Line:** 1466

```js
// BEFORE:
if (e.button !== 0 && e.pointerType !== "touch") return

// AFTER:
if (e.button !== 0 || (e.pointerType !== "touch" && e.pointerType !== "pen")) return
```

### Fix 3.3 — MEDIUM: 404 page "Return Home" link
**File:** `void/templates/404.html`
**Line:** 11

```html
<!-- BEFORE: -->
<a href="{{ config.site_url | default('/') }}" class="void-error__action">

<!-- AFTER: -->
<a href="{{ config.site_url | default('/', true) }}" class="void-error__action">
```

### Fix 3.4 — MEDIUM: Header logo missing alt text
**File:** `void/templates/partials/header.html`
**Lines:** 66, 68, 73, 75

```html
<!-- BEFORE: -->
<img src="..." alt="" ...>

<!-- AFTER (all four): -->
<img src="..." alt="{{ _brand }}" ...>
```

### Fix 3.5 — MEDIUM: Breadcrumbs root link
**File:** `void/templates/base.html`
**Line:** 637

```html
<!-- BEFORE: -->
<a class="void-breadcrumbs__link" href="{{ config.site_url }}">{{ config.site_name }}</a>

<!-- AFTER: -->
<a class="void-breadcrumbs__link" href="{{ config.site_url | default('/', true) }}">{{ config.site_name }}</a>
```

### Fix 3.6 — MEDIUM: SPA reinit missing action cluster
**File:** `void/templates/assets/javascripts/void.js`
**Lines:** 5199–5210

Add to the `inits` array in `reinitPageScoped()`:
```js
() => initActionCluster(_navConfig),
() => initConfigBuilder(_navConfig),
() => initConsent(_navConfig),
() => initAnnouncement(_navConfig),
```

---

## Execution Order

1. **Fix 3.1** (CRITICAL click guard) — highest priority, causes 404s
2. **Fix 1.1** (search URLs) — second highest, user-facing search broken
3. **Fix 2.2** (SW GitHub hosts) — avatars/popover caching
4. **Fix 2.1** (SW precache) — offline-first baseline
5. **Fix 2.3** (avatar lazy loading) — quick win
6. **Fix 2.4** (batch API calls) — popover performance
7. **Fix 3.2** (mermaid pan guard)
8. **Fix 3.3–3.5** (template URL/alt fixes)
9. **Fix 3.6** (SPA reinit)

## Verification

After all fixes:
- `mkdocs build --strict` — must pass
- `npm test` — must pass (may need update if void.test.js covers click guard)
- `python tools/check_docs.py` — must pass
- Manual test: search → click result → verify URL includes `/mkdocs-void/`
- Manual test: ctrl+click link → verify new tab opens (not SPA nav)
- Manual test: hover repo icon → verify popover loads fast (2 API calls first, 2 after)
