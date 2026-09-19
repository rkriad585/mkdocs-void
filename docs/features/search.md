---
date: 2026-09-19
title: Search
---

# Search

## What it is

Void ships a full-screen search modal powered by the built-in MkDocs search
plugin and a custom JavaScript layer. Press `/` to open, type to search, and
browse results with context snippets, highlighted terms, and a one-click
copy-link button on every result.

## When to use it

Search is always on by default. It's the fastest way to find a page, a
heading, or a specific term in the docs. The modal also supports deep links:
sharing `?q=term` in a URL re-opens search on arrival.

## How it works

The search modal is a full-screen overlay with a text input, result list, and
footer showing keyboard hints. The MkDocs search plugin generates a
`search/worker.js` file and a JSON index at build time. The Void theme's
`initSearch()` function creates a `Worker` pointing at that file, sends
queries as the user types, and renders results in real time.

| Step | What happens |
|------|-------------|
| Press `/` | `openSearch()` shows the overlay, focuses the input, and loads recent suggestions |
| Type ≥ 2 chars | The worker queries the MkDocs index and returns matching results |
| Result shown | Title with `<mark>` highlights, context snippet, breadcrumb path, icon, copy-link button |
| Press `Enter` | Navigates to the selected result |
| Press `Esc` | Closes the overlay and clears the URL `?q=` parameter |
| Copy-link button | Copies `pageURL?q=query` to clipboard, shows a toast confirmation |

## Configuration

```yaml
theme:
  void:
    search:
      enabled: true              # Render the search dialog (default true)
      shortcut_key: "/"          # Keyboard shortcut that opens search (default "/")
      placeholder: "Search..."   # Input placeholder
      min_chars: 2               # Minimum characters before searching (default 2)
      max_results: 10            # Maximum results to display (default 10)
      show_context: true         # Show context snippet under each result
      context_length: 120        # Characters of context per snippet (default 120)
      highlight_results: true    # Highlight search terms in results
      suggest: true              # Show recent-search suggestions
      style: "modal"             # "modal" | "dropdown" (future)
      ui:
        glass: true              # Glass morphism on the search dialog
        overlay_opacity: 0.5     # Backdrop overlay opacity
        show_shortcuts: true     # Show keyboard shortcut hints in footer
      result:
        show_icon: true          # Show page icon in results
        show_breadcrumb: true    # Show page path in results
        show_highlights: true    # Highlight terms inside matched text
        show_share: true         # Show "copy link" button on results
```

The shortcut is remappable under `theme.void.keyboard.shortcuts.search`:

```yaml
theme:
  void:
    keyboard:
      shortcuts:
        search:
          key: "/"               # default "/"
          label: "Open search"
```

## Under the hood

- **File:** `void.js` — `initSearch(config)` (line ~487)
- **Worker:** `new Worker(joinUrl(base, "search/worker.js"))` — the MkDocs search
  plugin generates this file at build time
- **Session:** last query stored in `void-session.search`; last 5 queries
  stored in `void-session.search_history`
- **Deep link:** `?q=term` re-opens search on arrival; the parameter is cleaned
  from the URL when search closes
- **Focus trap:** Tab cycles through the input, results, close button, and
  share buttons — never escapes the overlay
- **Config access:** `_config.void_search` (injected from `theme.void.search`)

## Accessibility notes

- The overlay is announced to screen readers; the input has a placeholder and
  an `aria-label`.
- Arrow keys (`↑`/`↓`) navigate results; `Enter` opens the selected result.
- Focus is trapped inside the modal and returned to the trigger element on close.
- The close button is labeled and activatable with `Esc`.