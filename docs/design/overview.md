---
date: 2026-09-07
title: Design System Overview
---

# Design System Overview

Void blends two design languages into one coherent system: the translucency and depth of **Glass** with the minimalism and grid-driven identity of **NothingOS**.

## Design Principles

1. **Depth through transparency** — Layers communicate hierarchy. Content sits behind glass; glass sits behind the canvas.
2. **Restraint over decoration** — Every visual element earns its place. The dot matrix, the borders, the blur — they all serve readability.
3. **Functional color** — Color is never decorative alone. Nothing Red signals interactivity. Monochrome tones carry structure.
4. **Typographic clarity** — One geometric sans for display, one monospace for code and labels. The pairing is intentional and consistent.

!!! note
    The theme avoids shadows as a primary depth cue. Translucency and blur replace drop shadows for most elevation work.

## Color System

Void defines a small, tightly controlled palette centered on Nothing Red (`#ff3030`) against a pure black canvas. Tokens are mapped to CSS custom properties on `:root` so they can be overridden without touching component styles.

See [Colors](colors.md) for the full token reference.

## Typography

The type system is built on two variable fonts from the Space family:

- **Space Grotesk** — headings, body text, UI labels
- **Space Mono** — code blocks, inline code, uppercase metadata labels

See [Typography](typography.md) for the type scale and usage rules.

## Glass Effects

Glass morphism is the core visual mechanic. Panels use `backdrop-filter: blur()` combined with semi-transparent backgrounds to create frosted surfaces.

Three intensity levels give you control over how much the glass "reads":

- **Light** — background barely visible, content stays flat
- **Medium** — balanced depth, the default
- **Heavy** — strong frosted effect, pronounced separation

See [Glass Effects](glass.md) for implementation details and CSS examples.

## Dot matrix

The NothingOS dot texture is a fixed, non-intrusive overlay drawn with two CSS
radial gradients, positioned behind every surface:

```css
:root {
  --void-dot-size: 2px;
  --void-dot-gap: 6px;
  --void-dot-opacity: 0.03;
  --void-dot-color: var(--void-text-primary);
}
```

Configure it from `theme.void.dot_matrix` (`enabled`, `size`, `gap`, `color`,
`opacity`, `position`). The default `enabled: true` ships the overlay in dark
mode and a lighter `0.02` opacity in light mode.

## Borders

A subtle 1px border is the standard surface edge — no heavy outlines:

```css
:root {
  --void-border-width: 1px;
  --void-border-style: solid;
  --void-glass-border: rgba(255, 255, 255, 0.18);
}
```

Adjusted with `theme.void.border` (`width: none|thin|thick`, `style:
solid|dashed|dotted`, `color`).

## Animations

Motion is token-driven and honors the OS:

```css
:root {
  --void-transition-duration: 250ms;
  --void-transition-easing: cubic-bezier(0.4, 0, 0.2, 1);
  --void-transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
  --void-transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
  --void-transition-spring: 500ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

- The `animation` token (`normal | reduced | none`) gates page transitions,
  hover effects, scroll progressives, and toast slide-ins.
- `prefers-reduced-motion: reduce` disables animation automatically for users
  who ask for it.

## Shadows

Shadows are a secondary depth cue — glass blur does the primary work:

```css
:root {
  --void-shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --void-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
  --void-shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
  --void-shadow-glass: 0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
}
```

See [Colors](colors.md) for the same table with usage notes.

## Spacing

A 4px base scale keeps rhythm predictable:

```css
:root {
  --void-space-1: 4px;
  --void-space-2: 8px;
  --void-space-3: 12px;
  --void-space-4: 16px;
  --void-space-5: 20px;
  --void-space-6: 24px;
  --void-space-8: 32px;
  --void-space-10: 40px;
  --void-space-12: 48px;
  --void-space-16: 64px;
}
```

Layout slots are tokens too: `--void-sidebar-width: 280px`,
`--void-toc-width: 240px`, `--void-header-height: 56px`,
`--void-content-max-width: 900px`, and `--void-section-gap: 40px` — all
configurable via `theme.void.spacing`.

## Radius

Precision rounding on the NothingOS scale:

```css
:root {
  --void-radius-sm: 4px;
  --void-radius-md: 8px;
  --void-radius-lg: 12px;
  --void-radius-xl: 16px;
  --void-radius-pill: 999px;
}
```

## Scrollbar

Native scrollbars are themed thin and quiet:

```css
:root {
  --void-scrollbar-thumb: var(--void-glass-border);
}
```

`theme.void.scrollbar` (`style: default|subtle|none`, `show`, `color`) controls
the appearance; setting `show: false` hides the native scrollbar.

## Selection

Text selection is a tokenized accent so even the "invisible" chrome matches the
brand — `theme.void.selection` (`background`, `color`) overrides the defaults.
This is styled via the standard `::selection` pseudo-class with the accent color.

## Components

The theme provides styled versions of common MkDocs components:

- [Buttons](../components/buttons.md)
- [Cards](../components/cards.md)
- [Forms](../components/forms.md)

All components inherit from the design tokens. Changing the accent color or glass intensity updates every component automatically.

!!! warning
    Custom components should use the CSS custom properties defined in `:root` rather than hardcoding values. This keeps your site consistent with theme updates.

## Architecture

```
void/
├── templates/
│   ├── assets/
│   │   ├── void.css              # Compiled output
│   │   ├── stylesheets/
│   │   │   ├── void.scss         # Design tokens, resets, glass, typography
│   │   │   └── components.scss     # All component styles
│   │   ├── javascripts/
│   │   │   └── void.js           # Theme JavaScript
│   │   └── images/
│   │       ├── logo.svg
│   │       └── favicon.svg
│   ├── partials/                   # HTML partials (header, nav, footer, etc.)
│   ├── base.html                   # Root template
│   └── mkdocs_theme.yml            # Theme registration
├── plugins/
│   └── void_plugin.py            # MkDocs plugin
└── __init__.py                     # Version
```

Everything is layered: tokens sit at the bottom, glass utilities in the middle, components on top. This keeps overrides predictable and conflict-free.
