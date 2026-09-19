---
date: 2026-09-19
title: "Level 3 — Customizer"
---

# Level 3 — Customizer

**Time:** ~half day

You'll override design tokens, configure component toggles, add custom CSS/JS,
and control page-level behavior.

## What you'll learn

- How to override the full design token system
- How to toggle components on/off via config
- How to add custom CSS and JavaScript
- How to use page-level overrides
- How to configure glass intensity

## Prerequisites

- Completed [Level 2 — Maker](maker.md)
- Comfort with CSS custom properties

## Step 1 — Override design tokens

Create `docs/stylesheets/custom.css`:

```css
:root {
  /* Brand colors */
  --void-accent: #6c5ce7;
  --void-accent-hover: #7c6cf7;

  /* Typography */
  --void-font-display: 'Inter', sans-serif;
  --void-font-body: 'Inter', sans-serif;
  --void-font-mono: 'JetBrains Mono', monospace;

  /* Glass */
  --void-glass-bg: rgba(108, 92, 231, 0.08);
  --void-glass-blur: 24px;
  --void-glass-border: rgba(108, 92, 231, 0.12);

  /* Spacing */
  --void-spacing-xs: 4px;
  --void-spacing-sm: 8px;
  --void-spacing-md: 16px;
  --void-spacing-lg: 24px;
  --void-spacing-xl: 32px;

  /* Shadows */
  --void-shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
  --void-shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
}
```

Add it to `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/custom.css
```

Every visual property in the theme flows from these tokens. Changing them
re-themes the entire site without touching component code.

## Step 2 — Toggle components

```yaml
theme:
  void:
    components:
      feedback:
        show: false                  # Disable feedback widget
      announcement_bar:
        show: false                  # Disable announcement bar
      cookie_consent:
        show: false                  # Disable cookie consent
      repo_popover:
        show: true                   # Enable repo popover
      prefetch:
        show: true                   # Enable prefetch-on-hover
```

Every component listed in `theme.void.components` can be toggled
independently.

## Step 3 — Configure glass intensity

```yaml
theme:
  void:
    glass:
      intensity: medium              # "light" | "medium" | "heavy"
```

Or override per-page in front matter:

```yaml
---
title: My Page
void_glass: heavy
---
```

## Step 4 — Add custom JavaScript

Create `docs/javascripts/extra.js`:

```javascript
document.addEventListener("DOMContentLoaded", function () {
  console.log("Custom JS loaded!")
})
```

Add it to `mkdocs.yml`:

```yaml
extra_javascript:
  - javascripts/extra.js
```

!!! warning
    Void's `void.js` runs in an IIFE and exposes no public API. Custom JS
    should hook into DOM events, not call Void internals.

## Step 5 — Page-level control

Every page supports these front matter keys:

```yaml
---
title: My Page
void_glass: light                   # Override glass intensity
void_toc: false                     # Hide TOC on this page
void_sidebar: false                 # Hide sidebar on this page
void_repo: false                    # Hide repo link on this page
void_footer: false                  # Hide footer on this page
---
```

## Step 6 — Keyboard shortcuts

Remap any shortcut:

```yaml
theme:
  void:
    keyboard:
      shortcuts:
        search:
          key: "Ctrl+K"             # Default is "/"
        toggle_sidebar:
          key: "Ctrl+B"             # Default is "Ctrl+Shift+B"
          persisted: true           # Remember collapsed state
      custom:
        - key: "g"
          label: "Go to top"
          action: "scroll_to_top"
```

## Verify you got it

- [ ] A custom accent color visible across the site
- [ ] A component toggled off (e.g., feedback widget hidden)
- [ ] Custom JS running in the browser console
- [ ] A page with overridden glass intensity
- [ ] A custom keyboard shortcut working

## Next level

Ready to contribute to Void itself? Continue to
[Level 4 — Contributor](contributor.md).

---

[Back to Learn](index.md)