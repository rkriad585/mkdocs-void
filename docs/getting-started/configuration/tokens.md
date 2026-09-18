---
title: Configuration - basics & design tokens
---

# Configuration - basics & design tokens

Generated from the live plugin tables (`_VOID_TOKEN_MAP`, `_void_defaults`, the `_VOID_DEFAULT_*` dicts and the compiled token defaults in `void.scss`) by `tools/emit_config_reference.py`. The page is regenerated in CI and can never drift from the shipped code.

<!-- generated: do not edit. Run `python tools/emit_config_reference.py`. -->

## Basics

- [animation](#themevoidanimation) &middot; [border](#themevoidborder) &middot; [dot_matrix](#themevoiddot_matrix) &middot; [glass](#themevoidglass) &middot; [highlight](#themevoidhighlight) &middot; [notes](#themevoidnotes)

### `theme.void.animation`
| | |
|---|---|
| Default | `"normal"` |
| Purpose | Entrance and hover animation intensity. |
| Example | `animation: "normal"   # "normal" | "reduced" | "none"` |

### `theme.void.border`
| | |
|---|---|
| Default | `"thin"` |
| Purpose | Glass panel border weight. |
| Example | `border: "thin"   # "thin" | "thick" | "none"` |

### `theme.void.dot_matrix`
| | |
|---|---|
| Default | `true` |
| Purpose | Toggles the dot-matrix NothingOS canvas behind the content. |
| Example | `dot_matrix: true` |

### `theme.void.glass`
| | |
|---|---|
| Default | `"medium"` |
| Purpose | Glass intensity: backdrop blur, saturation and panel opacity. |
| Example | `glass: "medium"   # "light" | "medium" | "heavy" | "none"` |

### `theme.void.highlight`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for syntax highlighting (highlight.js). |
| Example | `highlight: true` |

### `theme.void.notes`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the notes panel feature. |
| Example | `notes: true` |

## border_radius

- [border_radius.large](#themevoidborder_radiuslarge) &middot; [border_radius.medium](#themevoidborder_radiusmedium) &middot; [border_radius.small](#themevoidborder_radiussmall)

### `theme.void.border_radius.large`
| | |
|---|---|
| Default | `"12px"` |
| CSS variable | `--void-radius-lg` |
| Purpose | Large element corner radius. |
| Example | `border_radius: {large: "12px"}` |

### `theme.void.border_radius.medium`
| | |
|---|---|
| Default | `"8px"` |
| CSS variable | `--void-radius-md` |
| Purpose | Medium element corner radius. |
| Example | `border_radius: {medium: "8px"}` |

### `theme.void.border_radius.small`
| | |
|---|---|
| Default | `"4px"` |
| CSS variable | `--void-radius-sm` |
| Purpose | Small element corner radius. |
| Example | `border_radius: {small: "4px"}` |

## colors

- [colors.background](#themevoidcolorsbackground) &middot; [colors.border](#themevoidcolorsborder) &middot; [colors.overlay](#themevoidcolorsoverlay) &middot; [colors.primary](#themevoidcolorsprimary) &middot; [colors.primary_dark](#themevoidcolorsprimary_dark) &middot; [colors.primary_light](#themevoidcolorsprimary_light) &middot; [colors.surface](#themevoidcolorssurface) &middot; [colors.surface_light](#themevoidcolorssurface_light) &middot; [colors.text](#themevoidcolorstext) &middot; [colors.text_secondary](#themevoidcolorstext_secondary)

### `theme.void.colors.background`
| | |
|---|---|
| Default | `"#ffffff"` |
| CSS variable | `--void-ink` |
| Purpose | Page/canvas background color token. |
| Example | `colors: {background: "#000000"}` |

### `theme.void.colors.border`
| | |
|---|---|
| Default | `"transparent"` |
| CSS variable | `--void-glass-border` |
| Purpose | Glass panel border color token. |
| Example | `colors: {border: "rgba(255, 255, 255, 0.18)"}` |

### `theme.void.colors.overlay`
| | |
|---|---|
| Default | `"rgba(0, 0, 0, 0.5)"` |
| CSS variable | `--void-overlay-color` |

### `theme.void.colors.primary`
| | |
|---|---|
| Default | `"#ff3030"` |
| CSS variable | `--void-accent` |
| Purpose | Accent color for active states, links and progress. |
| Example | `colors: {primary: "#ff3030"}` |

### `theme.void.colors.primary_dark`
| | |
|---|---|
| Default | `"#c62828"` |
| CSS variable | `--void-accent-strong` |

### `theme.void.colors.primary_light`
| | |
|---|---|
| Default | `"rgba(255, 48, 48, 0.3)"` |
| CSS variable | `--void-accent-glow` |

### `theme.void.colors.surface`
| | |
|---|---|
| Default | `"transparent"` |
| CSS variable | `--void-glass-bg` |
| Purpose | Glass panel background color token. |
| Example | `colors: {surface: "rgba(255, 255, 255, 0.08)"}` |

### `theme.void.colors.surface_light`
| | |
|---|---|
| Default | `"transparent"` |
| CSS variable | `--void-glass-bg-strong` |

### `theme.void.colors.text`
| | |
|---|---|
| Default | `"#000000"` |
| CSS variable | `--void-text-primary` |
| Purpose | Primary text color token. |
| Example | `colors: {text: "#ffffff"}` |

### `theme.void.colors.text_secondary`
| | |
|---|---|
| Default | `"rgba(0, 0, 0, 0.7)"` |
| CSS variable | `--void-text-secondary` |

## shadows

- [shadows.large](#themevoidshadowslarge) &middot; [shadows.medium](#themevoidshadowsmedium) &middot; [shadows.small](#themevoidshadowssmall)

### `theme.void.shadows.large`
| | |
|---|---|
| Default | `"0 8px 32px rgba(0, 0, 0, 0.16)"` |
| CSS variable | `--void-shadow-lg` |

### `theme.void.shadows.medium`
| | |
|---|---|
| Default | `"0 4px 12px rgba(0, 0, 0, 0.12)"` |
| CSS variable | `--void-shadow-md` |

### `theme.void.shadows.small`
| | |
|---|---|
| Default | `"0 1px 2px rgba(0, 0, 0, 0.08)"` |
| CSS variable | `--void-shadow-sm` |
| Purpose | Small elevation shadow. |
| Example | `shadows: {small: "0 1px 2px rgba(0, 0, 0, 0.3)"}` |

## spacing

- [spacing.content_max_width](#themevoidspacingcontent_max_width) &middot; [spacing.content_padding](#themevoidspacingcontent_padding) &middot; [spacing.header_height](#themevoidspacingheader_height) &middot; [spacing.section_gap](#themevoidspacingsection_gap) &middot; [spacing.sidebar_width](#themevoidspacingsidebar_width) &middot; [spacing.toc_width](#themevoidspacingtoc_width)

### `theme.void.spacing.content_max_width`
| | |
|---|---|
| Default | `"900px"` |
| CSS variable | `--void-content-max-width` |
| Purpose | Article column max width. |
| Example | `spacing: {content_max_width: "720px"}` |

### `theme.void.spacing.content_padding`
| | |
|---|---|
| Default | `"40px 32px"` |
| CSS variable | `--void-content-padding` |

### `theme.void.spacing.header_height`
| | |
|---|---|
| Default | `"56px"` |
| CSS variable | `--void-header-height` |

### `theme.void.spacing.section_gap`
| | |
|---|---|
| Default | `"40px"` |
| CSS variable | `--void-section-gap` |

### `theme.void.spacing.sidebar_width`
| | |
|---|---|
| Default | `"280px"` |
| CSS variable | `--void-sidebar-width` |
| Purpose | Sidebar rail width. |
| Example | `spacing: {sidebar_width: "260px"}` |

### `theme.void.spacing.toc_width`
| | |
|---|---|
| Default | `"240px"` |
| CSS variable | `--void-toc-width` |
| Purpose | Table-of-contents rail width. |
| Example | `spacing: {toc_width: "220px"}` |

## transitions

- [transitions.duration](#themevoidtransitionsduration) &middot; [transitions.easing](#themevoidtransitionseasing)

### `theme.void.transitions.duration`
| | |
|---|---|
| Default | `"250ms"` |
| CSS variable | `--void-transition-duration` |
| Purpose | Default transition duration. |
| Example | `transitions: {duration: "300ms"}` |

### `theme.void.transitions.easing`
| | |
|---|---|
| Default | `"cubic-bezier(0.4, 0, 0.2, 1)"` |
| CSS variable | `--void-transition-easing` |
| Purpose | Default transition easing curve. |
| Example | `transitions: {easing: "cubic-bezier(0.4, 0, 0.2, 1)"}` |

## typography

- [typography.font_family](#themevoidtypographyfont_family) &middot; [typography.font_family_display](#themevoidtypographyfont_family_display) &middot; [typography.font_family_mono](#themevoidtypographyfont_family_mono) &middot; [typography.font_size_base](#themevoidtypographyfont_size_base) &middot; [typography.font_size_lg](#themevoidtypographyfont_size_lg) &middot; [typography.font_size_sm](#themevoidtypographyfont_size_sm) &middot; [typography.heading_letter_spacing](#themevoidtypographyheading_letter_spacing) &middot; [typography.heading_weight](#themevoidtypographyheading_weight) &middot; [typography.line_height](#themevoidtypographyline_height)

### `theme.void.typography.font_family`
| | |
|---|---|
| Default | `"'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif"` |
| CSS variable | `--void-font-body` |
| Purpose | Body font stack. Drives --void-font-body. |
| Example | `typography: {font_family: "Space Grotesk"}` |

### `theme.void.typography.font_family_display`
| | |
|---|---|
| Default | `"'Space Grotesk', sans-serif"` |
| CSS variable | `--void-font-display` |

### `theme.void.typography.font_family_mono`
| | |
|---|---|
| Default | `"'Space Mono', 'SF Mono', Consolas, monospace"` |
| CSS variable | `--void-font-mono` |
| Purpose | Code font stack. Drives --void-font-mono. |
| Example | `typography: {font_family_mono: "Space Mono"}` |

### `theme.void.typography.font_size_base`
| | |
|---|---|
| Default | `"16px"` |
| CSS variable | `--void-font-size-base` |
| Purpose | Base font size for article text. |
| Example | `typography: {font_size_base: "16px"}` |

### `theme.void.typography.font_size_lg`
| | |
|---|---|
| Default | `"18px"` |
| CSS variable | `--void-font-size-lg` |

### `theme.void.typography.font_size_sm`
| | |
|---|---|
| Default | `"14px"` |
| CSS variable | `--void-font-size-sm` |

### `theme.void.typography.heading_letter_spacing`
| | |
|---|---|
| Default | `"-0.02em"` |
| CSS variable | `--void-heading-letter-spacing` |

### `theme.void.typography.heading_weight`
| | |
|---|---|
| Default | `"700"` |
| CSS variable | `--void-heading-weight` |

### `theme.void.typography.line_height`
| | |
|---|---|
| Default | `"1.7"` |
| CSS variable | `--void-line-height` |

