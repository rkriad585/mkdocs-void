---
date: 2026-09-19
title: Focus Timer
---

# Focus Timer

## What it is

A built-in Pomodoro-style countdown timer. Press `Alt+Shift+T` to open
settings, start a session, and track your focus with a ring widget in the
TOC and a chip in reading mode. When the session ends, a toast and a
two-note chime signal completion.

## When to use it

Use the timer for timed reading or writing sessions — the default 25-minute
Pomodoro is a good starting point. The TOC widget shows a progress ring so
you can glance at the remaining time without leaving the article.

## How it works

The timer is a state machine with three phases: `idle` → `running` → `paused`.
The countdown is driven by `Date.now()` arithmetic (not `setInterval` drift),
so browser throttling never affects the elapsed time. A 1-second interval
repaints the UI surfaces.

On completion:

1. A success toast is shown ("Timer complete").
2. A two-note chime (A5/E5) plays via the Web Audio API.
3. If `document_title` is true, the tab title shows the elapsed time.
4. If `badge_in_cluster` is true, the action cluster badge shows remaining time.

## Configuration

```yaml
theme:
  void:
    timer:
      enabled: true                        # Master on/off (default true)
      default_minutes: 25                  # Session duration (default 25)
      persist: true                        # Remember state across reloads
      settings_popup: true                 # Show settings on Alt+Shift+T
      display_format: "mm:ss"              # "mm:ss" | "m:ss" | "SS"
      document_title: false                # Show countdown in the tab title
      start_with_reading: false            # Auto-start when reading mode activates
      badge_in_cluster: true               # Show remaining time in action cluster
      toc:
        show: true                         # Show the TOC ring widget
        position: "bottom"                 # "top" | "bottom"
        style: "ring"                      # "ring" | "bar" | "digits"
      reading:
        show: true                         # Show the reading-mode chip
      notifications:
        enabled: true                      # Enable completion notifications
        toast: true                        # Show a toast on completion
        sound: true                        # Play the completion chime
      colors:
        progress: "#8a5a33"                # Ring/chip progress color
```

Reader overrides are stored in `void-focus-timer-settings` and merged over
the author config on boot.

## Under the hood

- **File:** `void.js` — `initFocusTimer(config)` (line ~4545),
  `focusTimerStart()` (line ~4168), `focusTimerTick()` (line ~4270),
  `focusTimerComplete()` (line ~4282), `focusTimerRender()` (line ~4297)
- **localStorage keys:**
  - `void-focus-timer` — `{ remaining, running, updatedAt }` timer session
  - `void-focus-timer-settings` — reader overrides `{ default_minutes, toc_style, ... }`
- **UI surfaces:**
  - `.void-timer-toc` — ring/bar/digits widget in the TOC area
  - `.void-timer-reading` — small chip in reading mode
  - `--void-timer-progress` custom property drives the ring fill
  - `--void-timer-accent` set on `<html>` during an active session
- **Controls:** `[data-md-void-timer-ctrl="toggle|restart|cancel"]` buttons
  on the TOC widget
- **Shortcut:** `Alt+Shift+T` → `focusTimerToggle()` — opens settings popup
  when `settings_popup` is on, otherwise starts/pauses directly

## Accessibility notes

- Timer controls are real `<button>` elements with `aria-label` attributes.
- The completion chime is gated by `notifications.sound: true` — deafening
  readers is opt-in.
- The countdown is also available in the tab title (`document_title: true`)
  for screen readers that announce title changes.
- `prefers-reduced-motion: reduce` disables the ring animation.