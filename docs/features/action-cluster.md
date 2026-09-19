---
date: 2026-09-19
title: Action Cluster
---

# Action Cluster

## What it is

A floating action button (FAB) in the bottom corner that expands into a menu
of quick-access shortcuts: keyboard help, notes, focus timer, and reading mode.
Press `Alt+Shift+A` or click the FAB to open it.

## When to use it

The action cluster gives mobile and pointer-first readers a single tap point
for the most common overlays. It's especially useful when keyboard shortcuts
aren't available — touchscreens, tablets, or kiosk displays.

## How it works

The cluster renders a main FAB (`.void-action-cluster__main`, default icon
`plus`) and a menu of action buttons (`.void-action-cluster__action`). Each
action dispatches to the same `keyboardActions` registry that the keyboard
shortcuts use — so every built-in action (help, notes, timer, reading mode)
and every custom action registered through `keyboard.custom` is available.

The menu opens with a staggered animation and closes on:

- Selecting an action (`close_on_select`, default true)
- Pressing `Escape` (`close_on_escape`, default true)
- Clicking outside (`close_on_outside`, default true)

If fewer than `min_actions` (default 2) are enabled, the cluster is not
rendered.

## Configuration

```yaml
theme:
  void:
    action_cluster:
      enabled: true                        # Master on/off (default true)
      position: "bottom-left"              # "bottom-left" | "bottom-right"
      offset:
        bottom: "16px"
        left: "16px"                       # or right: "16px"
      main:
        icon: "plus"                       # plus | menu | help | notes | timer | reading | builder
        size: "44px"                       # FAB diameter
        glass: true                        # Glass background
        icon_transform: true               # Rotate icon 45° when open
      behavior:
        min_actions: 2                     # Don't render if fewer actions
        close_on_select: true              # Close after picking an action
        close_on_escape: true              # Close on Esc
        close_on_outside: true             # Close on outside click
        animation: "normal"                # "normal" | "reduced" | "none"
        tooltips: true                     # Show action labels on hover
        focus_trap: true                   # Trap focus inside the menu
      actions:
        - id: "keyboard_help"              # Dispatches to open_help
          icon: "help"
          label: "Keyboard shortcuts"
          shortcut: "?"
          enabled: true
          badge: "none"
        - id: "notes"                      # Dispatches to toggle_notes
          icon: "notes"
          label: "Open notes panel"
          shortcut: "Ctrl+Shift+N"
          enabled: true
          badge: "none"
        - id: "timer"                      # Dispatches to timer_toggle
          icon: "timer"
          label: "Focus timer"
          shortcut: "Alt+Shift+T"
          enabled: true
          badge: "time"                    # Show remaining time as badge
        - id: "reading_mode"               # Dispatches to toggle_reading_mode
          icon: "reading"
          label: "Reading mode"
          shortcut: "Alt+Shift+R"
          enabled: true
          badge: "none"
      replaces_notes_button: true          # Replace the header notes button
```

The shortcut is remappable under `theme.void.keyboard.shortcuts.toggle_action_cluster`.

## Under the hood

- **File:** `void.js` — `initActionCluster(config)` (line ~3919),
  `toggleActionCluster()` (line ~3773), `actionClusterDispatch(id)` (line ~3798)
- **Classes:** `.void-action-cluster`, `--open` state, `__main`, `__menu`,
  `__action`, `__tooltip`, `__badge`
- **Data attributes:** `data-md-void-action-cluster-position`,
  `data-md-void-action-cluster-tooltips`, `data-md-void-action-cluster-glass`,
  `data-md-void-action-cluster-transform`, `data-md-void-action-cluster-animation`
- **Dispatch:** each action button calls `actionClusterDispatch(id)`, which
  looks up the `keyboardActions` registry and invokes the matching function
  (`keyboard_help → open_help`, `notes → toggle_notes`, etc.)
- **Badge:** when `badge: "time"` and the timer is running, the remaining
  minutes are shown on the action button.

## Accessibility notes

- The FAB and every action button have `aria-label` attributes.
- The menu uses `role="group"` and focus is trapped when open.
- `Escape` closes the menu and returns focus to the FAB.
- The cluster respects `prefers-reduced-motion: reduce` (animation off).