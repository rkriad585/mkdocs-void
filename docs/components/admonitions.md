---
date: 2026-09-07
---

# Admonitions

## What it is

Void styles the standard MkDocs `admonition` extension, plus collapsible
`???` (details) blocks and inline variants. Every type maps to a themed accent
color and a small icon in the title.

## When to use it

Use admonitions for short, self-contained callouts that deserve visual weight
— a warning, a tip, a takeaway, a caution. Keep them short; if the content runs
longer than a few sentences, it probably belongs in prose instead. Prefer
collapsible details when the extra context is optional, and reserve `inline`
for tiny asides that should float beside text.

## In Markdown

Admonitions are plain Markdown. The type keyword follows `!!!` and the body is
indented:

```markdown
!!! note
    A note uses the accent purple color.
```

`???` renders a collapsible block, closed by default. Append `+` to default it
to open:

```markdown
??? note "Expand me"
    Hidden until expanded.
```

The `inline` class floats the block beside content:

```markdown
!!! note inline
    Floats to the left of the prose.
```

## Configuration

Admonitions come from the Markdown extensions, already enabled in the theme:

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

To switch the visual layer off site-wide, use the theme option. Custom types
stay available via CSS regardless:

```yaml
theme:
  void:
    admonitions:
      show: false        # default true — hides the styled layer
```

## Live preview / screenshot

### Note / Info / Example

```markdown
!!! note
    A generic note.
```

!!! note
    A generic note.

```markdown
!!! info
    Additional information.
```

!!! info "Custom title"
    Custom titles are supported.

```markdown
!!! example
    An example block.
```

!!! example
    An example block.

### Abstract / Summary / TLDR

```markdown
!!! abstract "Summary"
    A condensed takeaway.
```

!!! abstract "Summary"
    A condensed takeaway.

### Tip / Hint / Question / FAQ

```markdown
!!! tip
    A helpful tip.
```

!!! tip
    A helpful tip.

```markdown
!!! question
    A question worth asking.
```

!!! question
    A question worth asking.

### Success / Done / Check

```markdown
!!! success
    Everything worked.
```

!!! success
    Everything worked.

### Warning / Caution / Attention

```markdown
!!! warning
    Watch out.
```

!!! warning
    Watch out.

### Danger / Error / Failure / Bug / Important

```markdown
!!! danger
    This is destructive.
```

!!! danger
    This is destructive.

```markdown
!!! bug
    Known defect.
```

!!! bug
    Known defect.

```markdown
!!! important
    Really important requirement.
```

!!! important
    Really important requirement.

### Quote

```markdown
!!! quote
    "Less, but better." — Dieter Rams
```

!!! quote
    "Less, but better." — Dieter Rams

### Collapsible (details)

```markdown
??? note "Expand me"
    Hidden until expanded.
```

??? note "Expand me"
    Hidden until expanded.

```markdown
???+ danger
    Open by default and collapsible.
```

???+ danger
    Open by default and collapsible.

### Inline

```markdown
!!! note inline
    Floats to the left in this layout.
```

!!! note inline
    Floats to the left in this layout.

Paragraph text that wraps around the inline admonition demonstrates the
floating behavior. Copy continues to flow around the floated box, letting you
place short callouts against prose without breaking the reading flow.

## Under the hood

- Markdown output is the standard `<aside class="admonition note">` / details
  markup; Void restyles it in `components.scss` and wires the type color + icon
  through the `--void-icon` password-color token.
- The active type's title bar and icon read from `theme.void.admonitions.types`
  (`color` / `icon` per type) — empty values fall back to the built-in palette.
- Disabling the component sets `data-md-void-admonitions="false"` on the
  root element, which stops the icon/color layer without touching the
  underlying extension output.

## Accessibility notes

- The type is conveyed by both color and an icon, and the title text names the
  kind ("Warning:", "Danger:"), so meaning never relies on color alone.
- Collapsible blocks are native `<details>`/`<summary>` elements — keyboard
  focus and toggling work without custom scripting.
- Keep body text at normal contrast; the accent-colored title is a label, not
  body copy.