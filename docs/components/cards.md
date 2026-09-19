---
date: 2026-09-07
title: Cards
---

# Cards

## What it is

Cards are the primary content container in Void. Every card uses the glass
system to sit above the canvas with blur, border, and padding baked in.

## When to use it

Cards group related content into a scannable unit — feature callouts, image +
caption pairs, dashboard tiles, nested panels. Use the grid for multi-card
layouts that should reflow on their own. Avoid nesting heavy glass cards
inside other glass cards; layered blur can cause visual artifacts on some
browsers.

## In Markdown

Cards are raw HTML wrapped in `div` classes:

```html
<div class="void-card">
  <h3>Card title</h3>
  <p>Card body text goes here.</p>
</div>
```

For a responsive grid, wrap cards in `.void-card-grid`:

```html
<div class="void-card-grid">
  <div class="void-card">One</div>
  <div class="void-card">Two</div>
</div>
```

## Configuration

Cards respect the global glass setting (`theme.void.glass.intensity`) but can
be overridden per card with a modifier class:

```html
<div class="void-card void-card--light">Light glass</div>
<div class="void-card void-card--medium">Medium glass</div>
<div class="void-card void-card--heavy">Heavy glass</div>
```

Add `void-card--accent` for a 2 px solid accent top border that draws
attention to a highlighted card.

## Live preview / screenshot

### Default card

<div class="void-card">
  <h3>Card title</h3>
  <p>Card body text goes here.</p>
</div>

### Glass intensity

<div class="void-card void-card--light">
  <strong>Light</strong> &mdash; 6 px blur, good for sidebars and large panels.
</div>

<div class="void-card void-card--medium">
  <strong>Medium</strong> &mdash; default blur, suitable for most content.
</div>

<div class="void-card void-card--heavy">
  <strong>Heavy</strong> &mdash; 40 px blur, ideal for modals and floating panels.
</div>

### Accent border

<div class="void-card void-card--accent">
  <h3>Highlighted card</h3>
  <p>This card has an accent top border.</p>
</div>

### Card grid

<div class="void-card-grid">
  <div class="void-card">
    <h4>First card</h4>
    <p>Auto-fill with minmax(260px, 1fr) handles reflow without media queries.</p>
  </div>
  <div class="void-card">
    <h4>Second card</h4>
    <p>Each card grows to fill available space inside its column.</p>
  </div>
  <div class="void-card">
    <h4>Third card</h4>
    <p>The 16 px gap keeps everything breathable.</p>
  </div>
</div>

### Hover effect

Cards gain a subtle background and border-color change on hover. No
`transform: translateY()` is used, so there is no layout shift.

## Under the hood

- `.void-card` has 20 px padding, a 12 px border radius, and a 1 px border by
  default, drawn from the glass tokens (`--void-glass-bg`, `--void-glass-border`,
  `--void-radius-lg`).
- Intensity modifiers map to `--void-glass-blur` (light / medium / heavy);
  the theme's default is `medium` unless `theme.void.glass.intensity` overrides it.
- `.void-card-grid` uses `grid-template-columns: repeat(auto-fill, minmax(260px, 1fr))`
  with a 16 px gap — no media queries needed.

## Accessibility notes

- Cards are containers, not interactive widgets; put links and buttons inside
  them in normal document order so keyboard users reach them naturally.
- Do not hide a card behind `onclick` on the wrapper — a focusable control
  inside is the accessible pattern.
- Keep accent-bordered cards meaningful in grayscale: rely on the border and
  padding, not color, to signal emphasis.