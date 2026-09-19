---
date: 2026-09-19
title: Migration
---

# Migration

How to move an existing MkDocs project to Void — from a default theme, from
Material, or from Read the Docs.

## From default MkDocs theme

The default `mkdocs` theme has no customization layer. Migration is
straightforward:

1. **Install Void:**

   ```bash
   pip install mkdocs-void
   ```

2. **Switch the theme in `mkdocs.yml`:**

   ```yaml
   theme:
     name: void
   ```

3. **Remove theme-specific overrides.** If you had a `custom_dir` with
   overrides for the default theme, they won't apply to Void. Move any
   custom CSS into `extra_css` or a custom stylesheet.

4. **Build and verify:**

   ```bash
   mkdocs build --strict
   mkdocs serve
   ```

### What transfers automatically

- All Markdown content (no changes needed)
- `nav` structure
- `markdown_extensions` (pymdownx, admonitions, etc.)
- `plugins` configuration
- `extra_css` / `extra_javascript`

### What changes

- The visual design switches to Void's glass system
- Color scheme toggle is automatic (dark/light)
- Search uses Void's full-screen overlay (not the default sidebar search)
- Keyboard shortcuts are available (`/`, `?`, `Esc`)

## From Material for MkDocs

Material is the most common migration source. Void supports most of the same
Markdown extensions and pymdownx plugins, so content usually transfers
unchanged.

### Step-by-step

1. **Install Void:**

   ```bash
   pip install mkdocs-void
   ```

2. **Switch the theme:**

   ```yaml
   theme:
     name: void
   ```

3. **Keep your `markdown_extensions`.** Void supports the same pymdownx
   extensions (admonitions, tabs, code highlighting, footnotes, task lists,
   diagrams, math, etc.). No changes needed.

4. **Map Material-specific features:**

   | Material feature | Void equivalent |
   |-----------------|----------------|
   | `palette` toggle | Automatic dark/light toggle (no config needed) |
   | `features: navigation.tabs` | Void uses sidebar nav by default |
   | `features: search.suggest` | Void search includes suggestions |
   | `features: content.code.copy` | Void has built-in copy buttons |
   | `features: content.tabs.link` | Tabs sync via localStorage |
   | `icon` theme | Not supported — use `theme.logo` instead |
   | `font` customization | Configured via `theme.void.typography.font_family` |
   | `custom_dir` overrides | Move to `extra_css` / `extra_javascript` |

5. **Remove Material-specific keys** from `mkdocs.yml`:

   ```yaml
   # Remove these:
   palette:
     - scheme: default
       toggle: ...
   features:
     - navigation.tabs
     - search.suggest
   font:
     text: Roboto
   ```

6. **Build and verify:**

   ```bash
   mkdocs build --strict
   mkdocs serve
   ```

### What transfers automatically

- All Markdown content
- `nav` structure
- `markdown_extensions` and `pymdownx` config
- `plugins` configuration
- `extra_css` / `extra_javascript`
- `repo_url` / `repo_name`

### What changes

- Visual design switches to Void's glass system
- Color scheme toggle becomes automatic
- Search switches to Void's full-screen overlay
- Tab syncing, code copy, and keyboard shortcuts are built in

## From Read the Docs theme

The Read the Docs theme (`mkdocs-rtd-theme`) has a different structure:

1. **Install Void:**

   ```bash
   pip install mkdocs-void
   ```

2. **Switch the theme:**

   ```yaml
   theme:
     name: void
   ```

3. **Remove RTD-specific config:**

   ```yaml
   # Remove these:
   theme:
     name: rtd
     h1_underline: true
     logo_only: true
   ```

4. **Check `markdown_extensions`.** RTD uses some extensions that Void
   supports differently. The key ones:

   | RTD extension | Void support |
   |--------------|-------------|
   | `admonition` | ✅ Supported |
   | `pymdownx.details` | ✅ Supported |
   | `pymdownx.superfences` | ✅ Supported |
   | `toc` with `permalink` | ✅ Supported (Void adds anchor links automatically) |

5. **Build and verify:**

   ```bash
   mkdocs build --strict
   mkdocs serve
   ```

## From any theme —通用 checklist

Regardless of your current theme:

- [ ] Run `mkdocs build --strict` — zero warnings
- [ ] Verify dark/light mode toggle works
- [ ] Verify search returns results
- [ ] Verify keyboard shortcuts (`/`, `?`, `Esc`)
- [ ] Check mobile responsive layout
- [ ] Verify code blocks have copy buttons
- [ ] Verify tabs sync across the page
- [ ] Verify admonitions render correctly
- [ ] Check that `extra_css` and `extra_javascript` still load
- [ ] Verify `repo_url` link appears in the header

---

[Back to README](../index.md)