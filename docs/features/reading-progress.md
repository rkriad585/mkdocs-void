---
date: 2026-09-19
title: Reading Progress
---

# Reading Progress

## What it is

A thin progress bar at the top of the article that fills as you scroll down.
It gives a visual cue of how far you've read through a long page.

## When to use it

The progress bar is always on — no configuration needed. It's rendered by
the theme and driven by a scroll handler that sets the bar width to the
percentage of the article scrolled.

## How it works

`initScrollBehavior()` finds the `.void-progress__bar` element (rendered by
`base.html`) and on every scroll frame sets:

```javascript
progressBar.style.width =
  Math.min((scrollY / (docHeight - innerHeight)) * 100, 100) + "%"
```

The same handler also toggles `.void-header--scrolled` when `scrollY > 100`,
which applies a visual change to the header (border, opacity).

After SPA swaps, `updateScrollProgress()` recomputes the width immediately.

## Configuration

The progress bar has no per-feature config toggle — it's rendered whenever
the element exists in the markup. The author config mirror
`content.show_progress_bar` controls whether the template emits the element,
but the JS only acts if the element is present.

## Under the hood

- **File:** `void.js` — `initScrollBehavior()` (line ~1062),
  `updateScrollProgress()` (line ~5391)
- **Element:** `.void-progress__bar` — a `<div>` inside `.void-progress`
  rendered by `base.html`
- **Header:** `.void-header--scrolled` class toggled when `scrollY > 100`
- **No config gate:** the handler runs unconditionally; if the element
  doesn't exist, nothing happens.

## Accessibility notes

- The progress bar is a visual indicator only — it has no ARIA role and
  doesn't announce to screen readers.
- It doesn't interfere with scroll or focus behavior.