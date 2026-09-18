---
date: 2026-09-18
title: Getting Started
---

# Getting Started

Void goes from *installed* to *live* in under five minutes. This page is the
fastest possible path: install the theme, point one config file at it, serve,
then take a guided tour of every region of the page you now have.

## Install

Install the theme from PyPI — this installs both the theme and its companion
MkDocs plugin:

```bash
pip install mkdocs-void
```

## Quick setup

1. Scaffold a new project with Void's CLI:

   ```bash
   void new my-docs
   cd my-docs
   ```

   `void new` writes a ready-to-run project (`mkdocs.yml` + `docs/index.md`)
   with the theme and the `void` plugin already enabled — no manual wiring:

   ```yaml
   site_name: New Docs
   theme:
     name: void
     features:
       - navigation.sections
       - navigation.top
       - navigation.footer
       - content.code.copy
       - search.suggest
       - search.highlight
     void:
       glass: medium
       dot_matrix: true
       animation: normal
       border: thin
   plugins:
     - search
     - void
   ```

   Already have a MkDocs project? Just set `theme: {name: void}` and add
   `- void` to `plugins:` — zero custom CSS is required.

2. Start the dev server:

   ```bash
   mkdocs serve
   ```

3. Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## First look — a tour of the page regions

Everything below is already present on the page you just opened. The region
names are used throughout the docs, so learning them once pays off.

### The glass header

The top rail holds your logo or site name, a configurable **tagline** and
**version badge**, plus the right-side actions: **palette toggle**, **search**,
and the **repository link**. It is glass-frosted and sticky — it stays while
you scroll. Configure it under `theme.void.header`.

### The sidebar

The left glass column is the navigation tree: collapsible, with nested
indentation and an active-page accent. Fold it entirely with
`Ctrl+Shift+B`. Move the sidebar to the right-hand side with
`theme.void.sidebar.position`.

### The TOC rail

On wide screens the right column tracks the page's headings and highlights the
one you are reading (**scrollspy**), with permalinks on each heading. Fold it
with `Ctrl+Shift+T`. It carries two extra tools: the **focus timer** trigger
and the **repo popover** trigger. See `theme.void.toc`.

### The content column & reading progress

The center column shows the page, a **reading-progress bar** along the top
edge, and **prev/next** links at the foot. Long blocks of code get a **copy
button**; images zoom into a **lightbox**.

### The action cluster

A floating hub (the `+` button, bottom-right) expands into shortcuts: keyboard
help, notes, focus timer, and reading mode. Toggle it with `Alt+Shift+A`. All
actions are also reachable from the keyboard — press `?` for the full reference,
or open the [keyboard shortcuts](components/shortcuts.md) page.

### Full-screen search

Press `/` to open the modal: instant results, context snippets, term
highlighting, and a **copy-link** button per result. `Esc` closes it.

### Notes, focus timer & reading mode

- **Notes** (`Ctrl+Shift+N`) — a side panel for quick notes while you browse,
  with an optional time-to-live and export.
- **Focus timer** (`Alt+Shift+T`) — a session timer that lives in the TOC
  panel and pings you via a chime and toast when it completes.
- **Reading mode** (`Alt+Shift+R`) — hides the chrome (header, sidebars, TOC,
  footer, progress) and re-measures the article to full width for distraction-
  free reading. Your choice is remembered.

### The footer

Site footer with `default | minimal | extended` layouts: prev/next navigation,
social icons, custom columns, the copyright year (auto-injected), and the
optional **"Powered by Void"** credit + dot-matrix badge
(`extra.void_showcase: true`).

## Next steps

- [Model Project](getting-started/model-project.md) — a fully annotated example
  repo: folder layout, where assets live, and how config layers merge.
- [Configuration](getting-started/configuration.md) — every `theme.*` and
  `theme.void.*` key, generated from the plugin's own source.
- [Void Plugin](plugins/void.md) — the `search` + `void` plugin pair and the
  `- void:` settings surface.
- [Design System](design/overview.md) — how the glass, color, and typography
  tokens work under the hood.
- [Components](components/buttons.md) — the UI toolkit you can drop into any
  page.

---

[Back to README](index.md)