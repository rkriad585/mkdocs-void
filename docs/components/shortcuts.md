---
date: 2026-09-07
title: Keyboard Shortcuts
---

# Keyboard Shortcuts

## What it is

Press **`?`** anywhere in the documentation to open the keyboard shortcuts panel, which lists every binding.

## When to use it

Shortcuts are always available in the theme and require no configuration — they
are discoverable via `?`. They matter most for power users who navigate
documentation with the keyboard instead of the pointer.

## In Markdown

No Markdown needed — the shortcuts are global page furniture, registered by the
theme's script on every page.

## Configuration

The shortcuts ship enabled; there is no per-site switch. The panel itself is
rendered by the theme and lists the bindings below.

## Live preview / screenshot

### Global shortcuts

| Keys | Action |
|------|--------|
| `/` | Open search |
| `Esc` | Close active overlay (search, help, notes) |
| `?` | Show the keyboard shortcuts panel |

### Search

| Keys | Action |
|------|--------|
| `/` | Open search |
| `Enter` | Open the selected result |
| `↑` / `↓` | Navigate search results |
| `Esc` | Close search |

### Tabs

While a tab group is focused:

| Keys | Action |
|------|--------|
| `←` / `→` | Switch between tabs |

### Toggle overlays

| Keys | Action |
|------|--------|
| `Ctrl/Cmd + Shift + N` | Toggle the notes panel |
| `Ctrl/Cmd + Shift + B` | Toggle the sidebar (navigation) |
| `Ctrl/Cmd + Shift + T` | Toggle the table of contents |

> **Persistence**: Sidebar, TOC, and notes panel open/closed states are remembered
> in `localStorage` and restored on your next visit — independent of what other
> visitors see.

## Under the hood

- The help panel is the `.void-keyboard-help` overlay; `?` toggles it and the
  bindings are handled by the theme's global key handler.
- Overlay states (sidebar, TOC, notes) persist via `localStorage` keys and are
  restored on load.

## Accessibility notes

- All shortcuts mirror standard browser/document conventions (`/` search, `Esc`
  close, arrow keys) rather than hijacking common keys.
- Every shortcut target (search, notes, help) is reachable by pointer too, so
  keyboard bindings are enhancements, not the only path.
- To apply the classes yourself via the `attr_list` extension, see [CSS Classes in Markdown](classes.md).