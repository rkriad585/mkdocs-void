---
date: 2026-09-07
title: Trees
---

# Trees (Project Structure)

## What it is

Display a directory tree / project structure in a clean "file explorer" card. Void gives `tree` code blocks a glassy, monospace treatment with subtly dimmed comments.

## When to use it

Use trees to show a project layout, a module graph, or a config hierarchy —
anything that reads better as indented boxes-and-lines than as prose. Keep
trees shallow and trimmed to the relevant paths; deep dumps are better left to
generated tool output.

## In Markdown

Wrap the tree in a `tree` fenced code block:

````markdown
```tree
mkdocs-void/
├── void/                          # Python package
│   ├── __init__.py                  # Version (0.2.2)
│   ├── templates/
│   │   ├── base.html
│   │   ├── main.html
│   │   └── partials/
│   │       ├── header.html
│   │       └── toc.html
│   └── plugins/
│       └── void_plugin.py         # MkDocs plugin
├── docs/
│   ├── index.md
│   └── components/
├── mkdocs.yml
└── requirements.txt
```
````

## Configuration

No configuration is needed — a fenced ```tree``` block is styled out of the
box. To change the card's look, target the generated block in your custom
stylesheet:

```css
/* extra.css */
.highlight.language-tree {
  background: rgba(255, 255, 0, 0.04);
  border-color: var(--void-accent);
}
```

## Live preview / screenshot

```tree
mkdocs-void/
├── void/                          # Python package
│   ├── __init__.py                  # Version (0.2.2)
│   ├── templates/
│   │   ├── base.html
│   │   ├── main.html
│   │   └── partials/
│   │       ├── header.html
│   │       └── toc.html
│   └── plugins/
│       └── void_plugin.py         # MkDocs plugin
├── docs/
│   ├── index.md
│   └── components/
├── mkdocs.yml
└── requirements.txt
```

Trees pair well with the **Code Highlighting** and **Admonitions** components.
See [CSS Classes in Markdown](classes.md) to attach your own classes.

### Aligning comments

Pipe characters and spaces keep columns aligned. Use a monospace source editor; Void renders 1:1 with `white-space: pre`.

```tree
src/
├── core/
│   ├── engine.py        # entry point
│   └── parser.py        # tokenizer
└── ui/
    ├── app.js           # main view
    └── styles.js        # tokens
```

## Under the hood

- **Box-drawing support** — `├──`, `└──`, `│   ` glyphs render crisply in a monospace font.
- **Dimmed comments** — trailing `# comments` are shown in muted italic so they don't fight the tree lines.
- **File-explorer card** — each tree is wrapped in a subtle glass panel with rounded corners.
- **Scrollable** — long trees scroll horizontally instead of wrapping.

## Accessibility notes

- Content is real `<pre>` text, so the tree structure is selectable, copyable,
  and announced as code — no image or canvas fallback needed.
- Comment dimming is paired with no information loss: the comment text remains
  in the source and is readable, just visually de-emphasized.