---
date: 2026-09-07
title: Typography
---

# Typography

Void uses two typefaces from the Space family. Both are loaded from Google Fonts and served as variable fonts, and both are exposed as design tokens so you can swap the stack from a single override.

## Font tokens

The font stacks are design tokens on `:root`:

```css
--void-font-display: 'Space Grotesk', sans-serif;
--void-font-body: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
--void-font-mono: 'Space Mono', 'SF Mono', Consolas, monospace;
```

| Role | Token | Font | Use case |
|------|-------|------|----------|
| Display / body | `--void-font-display` / `--void-font-body` | Space Grotesk | Headings, body, UI labels |
| Mono | `--void-font-mono` | Space Mono | Code, inline code, metadata |

`theme.font.text` / `theme.font.code` in `mkdocs.yml` re-map these tokens (plus the Google Fonts `<link>`); `theme.void.typography.font_family` / `font_family_mono` are the plugin-level override path.

## Type scale

The scale is defined as CSS custom properties:

```css
--void-font-size-base: 16px;
--void-font-size-sm: 14px;
--void-font-size-lg: 18px;
```

| Token | Value | Typical use |
|-------|-------|-------------|
| `--void-font-size-sm` | `14px` | Small text, code, labels |
| `--void-font-size-base` | `16px` | Body copy (default) |
| `--void-font-size-lg` | `18px` | Lead paragraphs, larger callouts |

## Reading rhythm

Body text uses a relaxed line height with a slightly negative heading tracking:

```css
--void-line-height: 1.7;
--void-heading-weight: 700;
--void-heading-letter-spacing: -0.02em;
```

- **`--void-line-height: 1.7`** — the reading line height for body copy.
- **`--void-heading-weight: 700`** — the default heading weight.
- **`--void-heading-letter-spacing: -0.02em`** — tightens large headings so they read as one block.

## Labels and metadata

Small labels and metadata use Space Mono in uppercase with wide tracking:

```css
.label {
  font-family: var(--void-font-mono);
  font-size: var(--void-font-size-sm);
  text-transform: uppercase;
  letter-spacing: var(--void-heading-letter-spacing);
  color: var(--void-text-muted);
}
```

This convention is used for:

- Section headings above cards
- Badge text
- Table headers
- Breadcrumb separators

!!! note
    The uppercase mono style is reserved for short labels. Never use it for paragraphs or extended reading.

## Code blocks

Code uses Space Mono at small scale with the standard line height:

```css
.code-block {
  font-family: var(--void-font-mono);
  font-size: var(--void-font-size-sm);
  line-height: var(--void-line-height);
  tab-size: 2;
}
```

Inline code inherits the mono font but adds a subtle background:

```css
code {
  font-family: var(--void-font-mono);
  background: var(--void-ghost);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.9em;
}
```

## Heading hierarchy

Headings use Space Grotesk (via `--void-font-display`) with the default heading weight and letter-spacing:

| Element | Size  | Weight | Tracking |
|---------|-------|--------|----------|
| `h1`    | 2.25rem | 700  | tight (`-0.02em`) |
| `h2`    | 1.5rem  | 700  | tight (`-0.02em`) |
| `h3`    | 1.25rem | 700  | default |
| `h4`    | 1.125rem| 700  | default |

!!! tip
    Keep headings short. The type system is designed for clarity at a glance, not for long titling strings.

## Overriding the stack

Swap the whole type system from `mkdocs.yml`:

```yaml
theme:
  font:
    text: Inter
    code: JetBrains Mono
```

Or override the tokens directly in a custom stylesheet:

```css
:root {
  --void-font-display: 'Inter', sans-serif;
  --void-font-body: 'Inter', sans-serif;
  --void-font-mono: 'JetBrains Mono', monospace;
}
```

Any override updates every element that references these tokens — headings, body, labels, code, and inline code alike.