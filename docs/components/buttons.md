---
date: 2026-09-07
title: Buttons
---

# Buttons

## What it is

Void provides button classes built on the design tokens. All buttons use
Space Grotesk and inherit accent colors from the palette.

## When to use it

Use `.void-btn` for any actionable control that isn't a link — form submits,
demo triggers, in-page toggles. Pick **Pill** for the primary call to action,
**Accent** for the bordered secondary, and **Ghost** for the quietest option.
Keep one primary action per view; spare the accent treatment from everything
that isn't the main intent.

## In Markdown

Drop the class on a raw `<button>` (or an anchor styled as a button) anywhere
in your Markdown:

```html
<button class="void-btn">Default</button>
<button class="void-btn void-btn--accent">Accent</button>
<button class="void-btn void-btn--ghost">Ghost</button>
<button class="void-btn void-btn--pill">Pill</button>
```

Modifiers are used together freely: `class="void-btn void-btn--accent void-btn--pill"`.

## Configuration

No configuration is required — the classes are built into the theme. By
default, clicking any `.void-btn` shows a toast notification (e.g.
"Clicked: Default") and a pressed-scale feedback effect, wired up
automatically by `initUIExamples()` with no extra JavaScript.

## Live preview / screenshot

### Default

The standard filled button.

<div class="void-container" markdown>

<button class="void-btn">Default</button>

</div>

```html
<button class="void-btn">Default</button>
```

### Accent (outline)

A bordered variant with transparent background.

<div class="void-container" markdown>

<button class="void-btn void-btn--accent">Accent</button>

</div>

```html
<button class="void-btn void-btn--accent">Accent</button>
```

### Ghost

No background, no border. Muted text that highlights on hover.

<div class="void-container" markdown>

<button class="void-btn void-btn--ghost">Ghost</button>

</div>

```html
<button class="void-btn void-btn--ghost">Ghost</button>
```

### Pill

Rounded, filled, and prominent — best for key calls to action.

<div class="void-container" markdown>

<button class="void-btn void-btn--pill">Pill</button>

</div>

```html
<button class="void-btn void-btn--pill">Pill</button>
```

### Sizes

Add `--sm` or `--lg` to any variant to adjust size.

<div class="void-container" markdown>

<button class="void-btn void-btn--sm">Small</button>
<button class="void-btn">Default</button>
<button class="void-btn void-btn--lg">Large</button>

</div>

```html
<button class="void-btn void-btn--sm">Small</button>
<button class="void-btn">Default</button>
<button class="void-btn void-btn--lg">Large</button>
```

### Disabled

Add the native `disabled` attribute to dim and deactivate any button.

<div class="void-container" markdown>

<button class="void-btn" disabled>Disabled</button>
<button class="void-btn void-btn--accent" disabled>Disabled</button>
<button class="void-btn void-btn--ghost" disabled>Disabled</button>

</div>

```html
<button class="void-btn" disabled>Disabled</button>
<button class="void-btn void-btn--accent" disabled>Disabled</button>
<button class="void-btn void-btn--ghost" disabled>Disabled</button>
```

### Combining variants

Modifiers can be mixed freely.

<div class="void-container" markdown>

<button class="void-btn void-btn--accent void-btn--pill">Accent Pill</button>
<button class="void-btn void-btn--ghost void-btn--lg">Large Ghost</button>

</div>

```html
<button class="void-btn void-btn--accent void-btn--pill">Accent Pill</button>
<button class="void-btn void-btn--ghost void-btn--lg">Large Ghost</button>
```

## Under the hood

- Base class `.void-btn` plus modifiers `.void-btn--accent`, `--ghost`, `--pill`,
  `--sm`, `--lg` are defined in `components.scss` and color from
  `--void-accent` / `--void-ink` tokens.
- `initUIExamples()` (in the theme JS) attaches a click handler to every
  `.void-btn`: it shows the toast and applies the pressed-state scale, so demo
  buttons feel alive without setup.
- Native `disabled` handles both the dimmed look and pointer/keyboard blocking.

## Accessibility notes

- Always use a real `<button>` — never a `<div>` — so the control is natively
  focusable, activates with Space/Enter, and announces correctly.
- Don't remove focus styles; the theme keeps a visible focus ring on buttons.
- Disabled buttons use the native attribute; don't fake it with a class alone,
  and avoid repurposing it for loading states that need screen-reader feedback.