---
date: 2026-09-19
title: Back to Top
---

# Back to Top

## What it is

A floating button that appears in the bottom-right corner after you scroll
past 500 pixels. Click it to smooth-scroll back to the top of the page.

## When to use it

The back-to-top button is always on. It gives readers a quick way to return
to the top of a long article without manually scrolling or using the sidebar.

## How it works

`initBackToTop()` creates a `<button class="void-back-to-top">` (if one
doesn't already exist in the markup) with an `aria-label` from config. The
scroll handler in `initScrollBehavior()` toggles
`.void-back-to-top--visible` when `scrollY > threshold` (default 500px).

Clicking the button calls `window.scrollTo({ top: 0, behavior: "smooth" })`.

## Configuration

```yaml
theme:
  void:
    content:
      show_back_to_top: true        # Show the button (default true)
      back_to_top_label: "Back to top"  # aria-label text
      back_to_top_threshold: 500    # Scroll distance in px before showing (default 500)
```

## Under the hood

- **File:** `void.js` — `initBackToTop()` (line ~1102), visibility toggled
  inside `initScrollBehavior.onScroll` (line ~1083)
- **Element:** `.void-back-to-top` — created dynamically if not in markup
- **Visibility:** `.void-back-to-top--visible` toggled when `scrollY > threshold`
- **Config gate:** `componentShow("content", "show_back_to_top")` — absent
  defaults to on
- **Threshold:** `content.back_to_top_threshold` (default 500)

## Accessibility notes

- The button is a real `<button>` with an `aria-label` — screen readers
  announce it as "Back to top".
- Focus is not moved after clicking — the user stays in the document flow.
- `prefers-reduced-motion: reduce` disables the smooth scroll animation.