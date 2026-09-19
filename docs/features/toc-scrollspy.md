---
date: 2026-09-19
title: TOC Scrollspy
---

# TOC Scrollspy

## What it is

The "On this page" table of contents highlights the heading currently in
view. As you scroll through a long article, the active link in the TOC
updates automatically so you always know where you are.

## When to use it

Scrollspy is always on for pages with a TOC. It works automatically — no
configuration needed. It's especially valuable for long reference pages with
many H2/H3 headings.

## How it works

`initTocTracking()` attaches a rAF-throttled scroll handler that probes the
viewport at a configurable offset (default: 25% of the viewport height). The
active heading is the last one whose top is above the probe line. At the very
top of the page, the first heading is highlighted.

The active link is scrolled into view within the TOC container if it overflows.

## Configuration

```yaml
theme:
  void:
    toc:
      tracking:
        enabled: true                # Enable scrollspy (default true)
        offset: "100px"              # Scroll offset for activation (default 25% viewport)
      levels:                        # Heading levels to show
        h2: true
        h3: true
        h4: true
        h5: false
        h6: false
```

## Under the hood

- **File:** `void.js` — `initTocTracking()` (line ~976)
- **Algorithm:** not IntersectionObserver — a rAF-throttled scroll handler
  plus an immediate `refresh()` on page load and SPA swap
- **Probe line:** `window.scrollY + tracking_offset` or
  `window.scrollY + innerHeight * 0.25` (default)
- **Active class:** `.void-toc__link--active` — toggled on the matching `<a>`
- **Auto-scroll:** the active link is scrolled into view within the TOC
  container when it overflows (`scrollIntoView` with `block: "nearest"`)
- **Heading scope:** `toc.levels` config (default `"h2,h3,h4"`) — only
  listed levels participate in scrollspy

## Accessibility notes

- The active heading is indicated by a visual underline, not by color alone.
- Screen readers don't need the active state — they follow the user's scroll
  position naturally.
- The scrollspy doesn't interfere with keyboard navigation of the TOC links.