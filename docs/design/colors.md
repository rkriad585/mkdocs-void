---
date: 2026-09-07
title: Colors
---

# Colors

Void uses a token-based color system. Every color is a CSS custom property on `:root`, making the palette easy to override or extend.

## Core tokens

### Ink

The page background. Pure black — NothingOS signature.

```css
--void-ink: #000000;
```

### Text hierarchy

```css
--void-text-primary: #ffffff;
--void-text-secondary: rgba(255, 255, 255, 0.7);
--void-text-muted: #888888;
--void-text-accent: #ff3030;
```

### Ghost

Semi-transparent whites used for borders, dividers, and subtle surfaces.

```css
--void-ghost: rgba(255, 255, 255, 0.06);
--void-ghost-strong: rgba(255, 255, 255, 0.12);
```

### Accent

The primary interactive color — Nothing Red.

```css
--void-accent: #ff3030;
--void-accent-dim: rgba(255, 48, 48, 0.15);
--void-accent-glow: rgba(255, 48, 48, 0.3);
--void-accent-strong: #c62828;
--void-accent-strong-hover: #b71c1c;
```

### Glass

Background colors for glass panels:

```css
--void-glass-bg: rgba(255, 255, 255, 0.08);
--void-glass-bg-strong: rgba(255, 255, 255, 0.15);
--void-glass-border: rgba(255, 255, 255, 0.18);
--void-glass-border-strong: rgba(255, 255, 255, 0.35);
```

## Accent color

Void uses a single accent color — **Nothing Red** (`#ff3030`). It is used sparingly for interactive elements, focus states, and accent signals.

| Token | Hex | Usage |
|-------|-----|-------|
| `--void-accent` | `#ff3030` | Primary accent |
| `--void-accent-dim` | `rgba(255, 48, 48, 0.15)` | Faint accent backgrounds |
| `--void-accent-glow` | `rgba(255, 48, 48, 0.3)` | Glow effects |
| `--void-accent-strong` | `#c62828` | Solid fills/buttons (passes WCAG AA with white text) |
| `--void-accent-strong-hover` | `#b71c1c` | Strong-accent hover/active |

## Full token table

Every default token in dark mode, exactly as compiled from `void/templates/assets/stylesheets/void.scss`:

| Token | Dark default |
|-------|--------------|
| `--void-ink` | `#000000` |
| `--void-ghost` | `rgba(255, 255, 255, 0.06)` |
| `--void-ghost-strong` | `rgba(255, 255, 255, 0.12)` |
| `--void-text-primary` | `#ffffff` |
| `--void-text-secondary` | `rgba(255, 255, 255, 0.7)` |
| `--void-text-muted` | `#888888` |
| `--void-text-accent` | `#ff3030` |
| `--void-accent` | `#ff3030` |
| `--void-accent-dim` | `rgba(255, 48, 48, 0.15)` |
| `--void-accent-glow` | `rgba(255, 48, 48, 0.3)` |
| `--void-accent-strong` | `#c62828` |
| `--void-accent-strong-hover` | `#b71c1c` |
| `--void-glass-bg` | `rgba(255, 255, 255, 0.08)` |
| `--void-glass-bg-strong` | `rgba(255, 255, 255, 0.15)` |
| `--void-glass-border` | `rgba(255, 255, 255, 0.18)` |
| `--void-glass-border-strong` | `rgba(255, 255, 255, 0.35)` |

## Contrast rules

Void keeps every text/token pairing readable with these rules:

- **Body text on canvas** — `#ffffff` primary / `rgba(255, 255, 255, 0.7)` secondary on `#000000` comfortably exceeds WCAG AA (4.5:1) for normal text. `rgba(255, 255, 255, 0.7)` is intended for large text, labels, and secondary chrome, not long reading.
- **Nothing Red on black** — `#ff3030` on `#000000` exceeds 4.5:1 and is safe for links and interactive accents.
- **Accent-strong with white text** — `#c62828` is the solid-fill accent chosen to pass WCAG AA (4.5:1) with white labels; `#b71c1c` deepens it for hover/active.
- **Muted text** — `--void-text-muted: #888888` is decoration-only (captions, timestamps, metadata). Do not use it for required content.
- **Light mode** — the light palette swaps the same roles (`#000000` primary on `#ffffff`), preserving parity.

## Shadows

```css
--void-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
--void-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
--void-shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
--void-shadow-glass: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
```

## Overriding colors

Override any token in your `custom.css`:

```css
:root {
  --void-accent: #818cf8;
  --void-ink: #050510;
}
```

Add it to `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/custom.css
```

!!! tip
    Use the browser DevTools to inspect `:root` and find the exact token name you want to override. All tokens are prefixed with `--void-`.

## Light mode

When the palette scheme is set to `"default"`, the token values flip to their light-mode equivalents:

```css
[data-md-color-scheme="default"] {
  --void-ink: #ffffff;
  --void-text-primary: #000000;
  --void-text-secondary: rgba(0, 0, 0, 0.7);
  --void-text-muted: #767676;
  --void-ghost: rgba(0, 0, 0, 0.04);
  --void-ghost-strong: rgba(0, 0, 0, 0.08);
  --void-glass-bg: rgba(0, 0, 0, 0.05);
  --void-glass-bg-strong: rgba(0, 0, 0, 0.1);
  --void-glass-border: rgba(0, 0, 0, 0.12);
  --void-glass-border-strong: rgba(0, 0, 0, 0.25);
}
```

!!! warning
    Glass effects are less visible in light mode. Consider reducing blur intensity when using the light scheme.
