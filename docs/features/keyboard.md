---
date: 2026-09-19
title: Keyboard Reference
---

# Keyboard Reference

## What it is

Press **`?`** anywhere in the documentation to open the keyboard shortcuts
panel. The panel lists every active binding, built dynamically from the
current config — so custom shortcuts and disabled actions are always reflected
accurately.

## When to use it

The panel is the discoverability surface for keyboard-driven navigation. New
readers learn the shortcuts here; power users remap them under
`theme.void.keyboard` and the panel updates automatically.

## How it works

The global keydown handler watches for `?` (with Shift tolerance). When
detected, `toggleKeyboardHelp()` shows the `.void-keyboard-help` overlay and
builds the rows from:

1. Every enabled built-in shortcut (`search`, `close`, `search_up`,
   `search_down`, `search_open`, `tab_left`, `tab_right`, `toggle_sidebar`,
   `toggle_toc`, `toggle_notes`, `help`, `toggle_reading_mode`,
   `toggle_action_cluster`, `timer_toggle`, `toggle_scheme`,
   `toggle_repo_popover`)
2. Every entry in `keyboard.custom[]`
3. Every enabled `action_cluster.actions[]` shortcut (deduped against built-ins)

## Default shortcuts

| Shortcut | Action |
|----------|--------|
| `/` | Open search |
| `Esc` | Close active overlay |
| `↑` / `↓` | Navigate search results |
| `Enter` | Open the selected result |
| `←` / `→` | Switch between tabs |
| `Ctrl+Shift+B` | Toggle sidebar |
| `Ctrl+Shift+T` | Toggle table of contents |
| `Ctrl+Shift+N` | Toggle notes panel |
| `Ctrl+Shift+L` | Toggle color scheme |
| `Ctrl+Shift+G` | Toggle repo popover |
| `Alt+Shift+R` | Toggle reading mode |
| `Alt+Shift+A` | Toggle action cluster |
| `Alt+Shift+T` | Toggle focus timer |
| `?` | Show this panel |

## Configuration

Every shortcut is remappable under `theme.void.keyboard`:

```yaml
theme:
  void:
    keyboard:
      enabled: true                      # Master switch (default true)
      shortcuts:
        search:
          key: "/"                       # default "/"
          label: "Open search"
        toggle_sidebar:
          key: "Ctrl+Shift+B"            # default
          label: "Toggle sidebar"
          persisted: true                # Remember collapsed state (default true)
        toggle_toc:
          key: "Ctrl+Shift+T"
          label: "Toggle table of contents"
          persisted: true
        toggle_notes:
          key: "Ctrl+Shift+N"
          label: "Toggle notes panel"
        toggle_reading_mode:
          key: "Alt+Shift+R"
          label: "Toggle reading mode"
          persisted: true                # Remember reading mode (default true)
        toggle_action_cluster:
          key: "Alt+Shift+A"
          label: "Toggle action cluster"
        timer_toggle:
          key: "Alt+Shift+T"
          label: "Toggle focus timer"
        toggle_scheme:
          key: "Ctrl+Shift+L"
          label: "Toggle color scheme"
        toggle_repo_popover:
          key: "Ctrl+Shift+G"
          label: "Toggle repo popover"
        help:
          key: "?"
          label: "Show keyboard shortcuts"
      custom:
        - key: "g"
          label: "Go to top"
          action: "scroll_to_top"
```

Set `enabled: false` on any individual shortcut to disable it, or on the
whole `keyboard` block to disable all shortcuts at once.

## Under the hood

- **File:** `void.js` — `toggleKeyboardHelp()` (line ~3130),
  `keyboardHelpRows()` (line ~3060)
- **Classes:** `.void-keyboard-help`, `--visible` state, `__overlay`,
  `__panel`, `__header`, `__title`, `__close`, `__body`, `__row`,
  `__keys` (`<kbd>`), `__desc`
- **Config access:** `_config.keyboard` — the panel reads `kbdEnabled()`,
  `kbdKey()`, `kbdLabel()` for every shortcut and renders only enabled ones.
- **Key display:** `displayKey()` reformats combos — `Cmd` → `Ctrl/Cmd`,
  `Escape` → `Esc`, arrow keys → glyphs.
- **Custom actions:** each `keyboard.custom[]` entry with a `key`, `label`,
  and `action` is rendered as an additional row. Built-in action names:
  `scroll_to_top`, `toggle_sidebar`, `toggle_toc`, `toggle_notes`,
  `open_search`, `open_help`, `toggle_reading_mode`, `toggle_action_cluster`,
  `toggle_scheme`, `toggle_repo_popover`, `open_repo`.

## Accessibility notes

- The panel is announced as a dialog; `Esc` closes it and returns focus.
- Every row shows the key in a `<kbd>` element and a text description.
- The panel content is built from config, so it always reflects the actual
  bindings — no stale documentation.