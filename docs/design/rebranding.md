---
date: 2026-09-18
title: Rebranding
---

# Rebranding

This workshop walks a full brand swap end-to-end — the theme's "customizer"
path. You change five things in `mkdocs.yml` (plus one optional stylesheet) and
the entire site — tokens, header, sidebar, footer, and every component —
follows. No template editing, no JavaScript.

## What you will change

| Surface | Config key | What it controls |
|---------|------------|------------------|
| Accent | `theme.void.colors.primary` | Nothing Red → your brand color |
| Canvas | `theme.void.colors.background` | Pure black → your canvas |
| Glass | `theme.void.glass` | Frosted intensity everywhere |
| Type | `theme.font` | The two Space fonts → your stack |
| Logo | `theme.logo` / `theme.favicon` | Header mark + browser tab |
| Edge chrome | `theme.void` token groups | Borders, shadows, radius, scrollbar |

Every one of these lands as a CSS custom property on `:root`, which is exactly
why one config change re-skins the whole system.

## Step 1 — Pick your accent

Replace the default Nothing Red with your brand color. The theme ships five
accent slots so hover, focus, and dimmed states stay coherent:

```yaml
theme:
  void:
    colors:
      primary: "#6366f1"            # --void-accent, --void-text-accent
      primary_light: "#818cf8"      # --void-accent-glow (soft halo)
      primary_dark: "#4f46e5"       # --void-accent-strong (solid fills)
      dim: "rgba(99, 102, 241, 0.15)"   # --void-accent-dim (faint bg)
```

The instant the accent changes, links, active nav, progress bars, focus rings,
task-list checkmarks, timers, and the reading-mode signal all follow.

## Step 2 — Rebase the canvas

NothingOS lives on pure black. Move the whole site to your brand's canvas — or
keep black and only change the surface palette:

```yaml
theme:
  void:
    colors:
      background: "#0a0a12"         # --void-ink (dark scheme)
      text: "#f5f5ff"               # --void-text-primary
      text_secondary: "rgba(245, 245, 255, 0.7)"
      text_muted: "#8a8a99"
```

The glass tokens (`--void-glass-bg`, `--void-glass-border`) are translucent
whites that read correctly on any canvas, dark or light — you usually leave them
alone.

## Step 3 — Retune the glass

Glass intensity is a single switch. Use the object form for the three knobs:

```yaml
theme:
  void:
    glass:
      intensity: "medium"           # light | medium | heavy | none
      blur: true                    # set false for a flat, opaque-feel panel
      blur_amount: "12px"           # custom radius, overrides intensity blur
      opacity: 0.85                 # scales every glass fill opacity
      saturation: true              # backdrop saturate() on/off
```

## Step 4 — Swap the type system

The two Space fonts become your fonts in one block. This updates the Google
Fonts `<link>` *and* the compiled `--void-font-body` / `--void-font-mono`
tokens:

```yaml
theme:
  font:
    text: Inter
    code: JetBrains Mono
```

Overrides by component, if you only want to touch headings:

```yaml
theme:
  void:
    typography:
      font_family_display: Inter
      heading_weight: 800
      heading_letter_spacing: "-0.01em"
```

## Step 5 — Swap the logo and favicon

Drop in your marks (dark/light variants are honored, and header/sidebar/footer
all reuse the same files):

```yaml
theme:
  logo: assets/images/my-logo.svg          # macro light-mode logo
  favicon: assets/images/my-favicon.svg

extra:
  void_logo_dark: assets/images/my-logo.svg
  void_logo_light: assets/images/my-logo-light.svg
  void_favicon_dark: assets/images/my-favicon.svg
  void_favicon_light: assets/images/my-favicon-light.svg
```

## Step 6 — Edge chrome (tokens)

Now the details that make a brand feel finished — borders, radius, shadows, and
the scrollbar:

```yaml
theme:
  void:
    border:
      width: thin                    # none | thin | thick
      style: solid                   # solid | dashed | dotted
      color: "rgba(99, 102, 241, 0.2)"
    shadows:
      enabled: true                  # keep glass shadows on
    scrollbar:
      show: false                    # hide the native scrollbar
      color: "#6366f1"               # thumb color
    selection:
      background: "#6366f1"
      color: "#ffffff"
```

## Step 7 — Verify parity

```bash
mkdocs serve
```

Then check four spots:

1. **Header** — logo, site name, glass rail, active nav underline in the new accent.
2. **Sidebar** — active border, icon tint, hover state.
3. **Footer** — divider, social icons, prev/next arrows.
4. **A component page** — buttons, admonitions, and tables should all pick up the accent and glass automatically.

## The one-config wholesale swap

The full change composes into a single `theme.void` block that re-brands the
entire site:

```yaml
theme:
  name: void
  logo: assets/images/my-logo.svg
  favicon: assets/images/my-favicon.svg
  font:
    text: Inter
    code: JetBrains Mono
  void:
    colors:
      primary: "#6366f1"
      primary_light: "#818cf8"
      primary_dark: "#4f46e5"
      background: "#0a0a12"
    glass:
      intensity: medium
    border:
      width: thin
    scrollbar:
      show: false
```

That is the whole workshop — swap tokens, not templates. See [Overview](overview.md)
for the full token list and [Colors](colors.md) for contrast guidance.