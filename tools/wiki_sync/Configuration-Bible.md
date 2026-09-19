# Configuration Bible

The full `theme.void` config surface. Every key, its default, and what it does.

## Theme basics

```yaml
theme:
  name: void
  language: en
  palette:
    - media: "(prefers-color-scheme: dark)"
      scheme: default
    - media: "(prefers-color-scheme: light)"
      scheme: slate
  font:
    text: Space Grotesk
    code: Space Mono
  icon:
    logo: material/book-open-page-variant
```

## Void-specific (`theme.void`)

### Glass

```yaml
theme:
  void:
    glass:
      intensity: medium          # "light" | "medium" | "heavy"
```

### Reading mode

```yaml
theme:
  void:
    reading_mode:
      enabled: true
      persisted: true            # Remember across visits
      sections:                  # Heading levels to hide
        h2: false
        h3: false
```

### Keyboard

```yaml
theme:
  void:
    keyboard:
      enabled: true
      shortcuts:
        search:
          key: "/"
          label: "Open search"
        toggle_sidebar:
          key: "Ctrl+Shift+B"
          persisted: true
      custom:
        - key: "g"
          label: "Go to top"
          action: "scroll_to_top"
```

### Components

```yaml
theme:
  void:
    components:
      feedback:
        show: true
        title: "Was this page helpful?"
        positive: "Yes!"
        negative: "No!"
        github_labels: ["feedback"]
      announcement_bar:
        show: true
        text: "New in v0.2 — glass components!"
        dismissable: true
        position: "bottom"       # "top" | "bottom" | "left" | "right" | "center"
      cookie_consent:
        show: true
        message: "We use cookies for analytics."
        accept_label: "Accept"
        decline_label: "Decline"
        position: "bottom"
      repo_popover:
        show: true
        fields:                  # Which fields to show (default: all)
          - stars
          - forks
      prefetch:
        show: true
        external: false
        exclude: []
      highlighting:
        cdn_url: "..."
        cdn_css_url: "..."
```

### Content

```yaml
theme:
  void:
    content:
      show_progress_bar: true
      show_back_to_top: true
      back_to_top_label: "Back to top"
      back_to_top_threshold: 500
      task_lists:
        persist_state: true
      typography:
        image_lightbox: true
```

### Typography

```yaml
theme:
  void:
    typography:
      font_family: "Space Grotesk"
      font_family_mono: "Space Mono"
```

### TOC

```yaml
theme:
  void:
    toc:
      tracking:
        enabled: true
        offset: "100px"
      levels:
        h2: true
        h3: true
        h4: true
```

### Timer

```yaml
theme:
  void:
    timer:
      enabled: true
      persist: true
      default_minutes: 25
```

### Search

```yaml
theme:
  void:
    search:
      enabled: true
      min_chars: 2
      result:
        show_share: true
```

### PWA

```yaml
theme:
  void:
    pwa:
      manifest: true
      display: "standalone"
      icons: true
      theme_color: ""
      background_color: "#111114"
```

### i18n

```yaml
theme:
  void:
    i18n:
      search_placeholder: "Search docs..."
      toc_title: "On this page"
```

Full reference: [https://rkriad585.github.io/mkdocs-void/getting-started/configuration/](https://rkriad585.github.io/mkdocs-void/getting-started/configuration/)