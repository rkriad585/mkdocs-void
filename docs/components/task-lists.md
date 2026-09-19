---
date: 2026-09-07
---

# Task Lists

## What it is

Void styles `pymdownx.tasklist` checklist items with the glass theme and
makes them interactive, persisting your checked state across page reloads in
the browser (localStorage, keyed per page).

## When to use it

Use task lists for checklists that readers may tick off — progress tracking,
feature status, "before you start" steps. They are interactive eye-candy by
default; for non-interactive toggles (e.g. an FAQ checklist), switch
`persist_state` off (see below).

## In Markdown

```markdown
- [ ] not started
- [x] completed
- [X] also completed
```

## Configuration

Task lists are provided by `pymdownx.tasklist` (enabled in the theme) and
tuned under `theme.void.content.task_lists`:

```yaml
theme:
  void:
    content:
      task_lists:
        enabled: true        # default true
        custom_checkbox: true
        persist_state: true  # remember ticks in localStorage per page
```

## Live preview / screenshot

- [x] Design tokens defined
- [x] Admonitions expanded
- [ ] Tabs finalized
- [ ] Mermaid integration
- [ ] Notes & annotations

> Check a box, then reload the page — your selection is remembered.

## Under the hood

- List items are `pymdownx.tasklist` checkbox markup restyled with the glass
  tokens and the accent palette.
- The checked state is written back to localStorage as a `"1"`/`"0"` flag under
  `void-task.*` keys, keyed per page.
- There is no server-side storage; clearing site data (or the `void-task.*`
  keys) resets the state.

## Accessibility notes

- Items remain real checkboxes, so they are natively focusable, toggle with
  Space, and are announced to screen readers.
- The accent checkmark is paired with the native checked state, so status is
  never conveyed by color or icon alone.