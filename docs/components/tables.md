---
date: 2026-09-07
title: Tables
---

# Tables

## What it is

Tables are styled out of the box by the theme. Standard Markdown (PHP-Markdown style) tables, as well as raw `<table>` elements, get the glass treatment: a distinct header row, uppercase monospace header labels, row hover highlighting, and a responsive scroll wrapper.

## When to use it

Use tables for tabular data that benefits from row/column scanning — feature
matrices, version support, API fields, comparison lists. Keep cells short and
aligned; for long-form prose a table is rarely the right shape.

## In Markdown

The simplest way to create a table is with Markdown:

```markdown
| Feature           | Status      | Notes                         |
|-------------------|-------------|-------------------------------|
| Admonitions       | Done        | Full Material family + icons  |
| Tabs              | Done        | Keyboard navigable, unlimited |
| Task Lists        | Done        | Persisted to localStorage     |
| Mermaid Diagrams  | Done        | Themed dark/light rendering   |
```

Markdown supports left, center, and right column alignment via the separator row:

```markdown
| Left          | Center          | Right |
|:--------------|:---------------:|------:|
| Alpha         | Beta            |  100% |
| Gamma         | Delta           |   50% |
```

## Configuration

For more control, use a raw HTML table and add the `void-table` class (and optionally wrap it in a `void-table__wrap` for responsive scrolling):

```html
<div class="void-table__wrap">
  <table class="void-table">
    <thead>
      <tr><th>Keyboard</th><th>Action</th></tr>
    </thead>
    <tbody>
      <tr><td>Ctrl+Shift+N</td><td>Toggle the Notes panel</td></tr>
      <tr><td>Ctrl+Shift+B</td><td>Toggle the navigation sidebar</td></tr>
    </tbody>
  </table>
</div>
```

Presentation options exist under `theme.void.content.tables`:

```yaml
theme:
  void:
    content:
      tables:
        responsive: true    # wrap in a scroll container on narrow screens
        striped: false
        bordered: false
```

## Live preview / screenshot

### Markdown table

| Feature           | Status      | Notes                         |
|-------------------|-------------|-------------------------------|
| Admonitions       | Done        | Full Material family + icons  |
| Tabs              | Done        | Keyboard navigable, unlimited |
| Task Lists        | Done        | Persisted to localStorage     |
| Mermaid Diagrams  | Done        | Themed dark/light rendering   |

### Aligned Columns

| Left          | Center          | Right |
|:--------------|:---------------:|------:|
| Alpha         | Beta            |  100% |
| Gamma         | Delta           |   50% |

### Hover Interaction

Rows highlight on hover and the header is a distinct glass band:

| Package       | Version | Python |
|---------------|:-------:|:------:|
| mkdocs        |  1.6    |  >=3.8 |
| pymdownx      |  10.9   |  >=3.8 |
| highlight.js  |  11.9   |   n/a  |

### HTML Table with Classes

<div class="void-table__wrap">
  <table class="void-table">
    <thead>
      <tr>
        <th>Keyboard</th>
        <th>Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>N</kbd></td>
        <td>Toggle the Notes panel</td>
      </tr>
      <tr>
        <td><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd></td>
        <td>Toggle the navigation sidebar</td>
      </tr>
    </tbody>
  </table>
</div>

## Under the hood

- **`.void-table__wrap`** — adds a scrollable container so wide tables scroll horizontally on small screens.
- Plain `<table>` (Markdown output) is styled identically without needing any class.
- Header cells use the theme's mono font and uppercase tracking for a consistent technical look.

## Accessibility notes

- Markdown tables compile to real `<table>` markup with `<th>` header cells,
  so screen readers announce row/column structure.
- `.void-table__wrap` keeps wide tables usable on small screens without
  squashing content; the header band plus hover remain meaningful in
  grayscale, so row tracking never depends on color alone.