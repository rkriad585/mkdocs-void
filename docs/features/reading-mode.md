---
date: 2026-09-19
title: Reading Mode
---

# Reading Mode

## What it is

Press `Alt+Shift+R` to enter a distraction-free reading view that hides the
header, sidebar, TOC, footer, and progress bar. The article widens to fill
the viewport and the typography switches to a comfortable reading measure.

## When to use it

Reading mode is ideal for long-form content — tutorials, deep-dives, and
reference pages that benefit from the full width. Toggle it on when you want
to focus on prose without chrome, and toggle it off when you need navigation
back.

## How it works

`toggleReadingMode()` sets `data-md-void-reading="active"` on `<html>` and
adds the `void-reading-mode` class to `<body>`. The compiled CSS then hides
the configured sections and applies reading typography — no DOM nodes are
removed, only hidden via CSS. The view retains the active color scheme.

On entering reading mode:

1. Header, sidebar, TOC, footer, and progress bar are hidden (per config).
2. The article is re-measured to `reading_mode.typography.measure` (default `100%`).
3. If `reading_mode.notes.open_on_enter` is true, the notes panel opens.
4. If `reading_mode.start_with_reading` is true and the timer is idle, the
   focus timer auto-starts.

On exiting, all sections reappear and the article returns to normal width.

## Configuration

```yaml
theme:
  void:
    reading_mode:
      enabled: true                    # Master on/off (default true)
      shortcut_key: "Alt+Shift+R"      # Keyboard shortcut (default Alt+Shift+R)
      persisted: true                  # Remember state across reloads (default true)
      sections:
        header: true                   # Hide the header
        sidebar: true                  # Hide the navigation sidebar
        toc: true                      # Hide the "On this page" rail
        footer: true                   # Hide the footer
        progress: true                 # Hide the reading progress bar
      notes:
        show: true                     # Keep notes panel available
        open_on_enter: false           # Auto-open notes when entering reading mode
      typography:
        font_size: "1.125rem"          # Article font size in reading mode
        line_height: "1.75"            # Article line height
        measure: "100%"                # Max article width (e.g. "70ch")
      scheme:
        colors:                        # Optional palette overrides
          # background: "#0a0a12"      # --void-ink
          # text: "#f5f5ff"            # --void-text-primary
```

The shortcut is remappable under `theme.void.keyboard.shortcuts.toggle_reading_mode`.

## Under the hood

- **File:** `void.js` — `initReadingMode(config)` (line ~2862),
  `toggleReadingMode()` (line ~2823), `readingModeSet(active)` (line ~2836)
- **CSS:** `html[data-md-void-reading="active"]` rules in `components.scss`
  hide the sections and apply typography overrides.
- **Persistence:** `void-ui-reading` (`"1"`/`"0"`) — only written when
  `reading_mode.persisted` is true (default true).
- **State attribute:** `data-md-void-reading` on `<html>` — values `"active"`
  or `"off"`.
- **Boot restore:** if persisted and `"1"`, `readingModeSet(true)` runs at
  startup before the first paint.

## Accessibility notes

- Reading mode is a visual toggle, not a structural one — screen readers
  still see the full DOM; only visual chrome is hidden.
- The keyboard shortcut is configurable and can be disabled individually.
- `prefers-reduced-motion: reduce` disables the transition animation.