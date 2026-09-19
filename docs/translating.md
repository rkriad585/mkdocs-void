---
date: 2026-09-19
title: Translating Void
---

# Translating Void

How to translate every UI string in the theme — search labels, TOC titles,
timer controls, repo popover labels, and more.

## How it works

All chrome strings live in `_VOID_DEFAULT_I18N` (`void/plugins/void_plugin.py`)
and are overridable per site via `theme.void.i18n`. The JS reads them at
runtime via `t("group.key", "fallback")`.

Unknown keys **abort the build** — this catches typos instead of silently
leaving strings in English.

## Flat aliases

The documented config uses flat keys under `theme.void.i18n`:

| Flat key | Group | Child | Default |
|----------|-------|-------|---------|
| `search_placeholder` | search | placeholder | "Type to start searching..." |
| `search_results` | search | results | "Results" |
| `search_no_results` | search | noResults | "No results found" |
| `search_start_typing` | search | startTyping | "Start typing..." |
| `search_loading` | search | loading | "Loading" |
| `search_load_error` | search | loadError | "Failed to load" |
| `search_suggestions` | search | suggestions | "Suggestions" |
| `toc_title` | toc | title | "On this page" |
| `back_to_top` | toc | backToTop | "Back to top" |
| `copy_to_clipboard` | clipboard | copy | "Copy" |
| `copied_to_clipboard` | clipboard | copied | "Copied" |
| `copy_link` | clipboard | copyLink | "Copy link" |
| `link_copied` | clipboard | linkCopied | "Link copied" |
| `comments_title` | comments | title | "Comments" |
| `skip_to_content` | a11y | skipToContent | "Skip to content" |
| `breadcrumb_label` | a11y | breadcrumb | "Breadcrumb" |
| `previous_page` | footer | previous | "Previous" |
| `next_page` | footer | next | "Next" |
| `footer_powered_by` | footer | poweredBy | "Powered by" |

## Example — French

```yaml
theme:
  void:
    i18n:
      search_placeholder: "Rechercher..."
      toc_title: "Sur cette page"
      back_to_top: "Retour en haut"
      copy_to_clipboard: "Copier"
      copied_to_clipboard: "Copie"
      previous_page: "Precedent"
      next_page: "Suivant"
      footer_powered_by: "Propulse par"
```

## Full string inventory

Beyond the flat aliases, the nested groups contain additional keys. Use
the nested syntax in `theme.void.i18n` to override them:

### Clipboard

```yaml
theme:
  void:
    i18n:
      clipboard:
        copy: "Copy"
        copied: "Copied"
        copyLink: "Copy link"
        linkCopied: "Link copied"
        copyLinkFailed: "Copy failed"
```

### Zoom (image lightbox)

```yaml
theme:
  void:
    i18n:
      zoom:
        preview: "Preview"
        close: "Close"
        previous: "Previous"
        next: "Next"
        zoomIn: "Zoom in"
        zoomOut: "Zoom out"
        copyImage: "Copy image"
        downloadImage: "Download image"
```

### Repo popover

```yaml
theme:
  void:
    i18n:
      repo:
        status: "Status"
        noPublicData: "No public data"
        loadError: "Failed to load"
        licenseNone: "None"
        latestTag: "Latest tag"
        author: "Author"
        followers: "Followers"
        publicRepos: "Public repos"
        location: "Location"
        stars: "Stars"
        watchers: "Watchers"
        forks: "Forks"
        openIssues: "Open issues"
        language: "Language"
        license: "License"
        defaultBranch: "Default branch"
        commits: "Commits"
        tags: "Tags"
        latestCommit: "Latest commit"
        commitMsg: "Last commit msg"
        created: "Created"
        updated: "Last updated"
        pushed: "Last pushed"
```

### Notes panel

```yaml
theme:
  void:
    i18n:
      notes:
        notes: "Notes"
        close: "Close"
        add: "Add note"
        exportMd: "Export MD"
        exportJson: "Export JSON"
        placeholder: "Add a note..."
        cancel: "Cancel"
        save: "Save"
        saveChanges: "Save changes"
        colorPrefix: "Color:"
        delete: "Delete"
        empty: "No notes"
```

### Focus timer

```yaml
theme:
  void:
    i18n:
      timer:
        focus: "Focus"
        title: "Focus timer"
        settings: "Settings"
        close: "Close"
        sessionLength: "Session length"
        tocStyle: "TOC style"
        tocPosition: "TOC position"
        readingChip: "Reading"
        toastNotify: "Notify when done"
        chime: "Chime"
        cancel: "Cancel"
        startSession: "Start session"
        start: "Start"
        restart: "Restart"
        stop: "Stop"
        reset: "Reset"
        controls: "Controls"
        complete: "Done!"
        ring: "Ring"
        bar: "Bar"
        digits: "Digits"
        top: "Top"
        bottom: "Bottom"
```

### Navigation and help

```yaml
theme:
  void:
    i18n:
      navigation:
        label: "Navigation"
      help:
        title: "Keyboard shortcuts"
      footer:
        previous: "Previous"
        next: "Next"
        poweredBy: "Powered by"
```

## How to add a new language

1. **Find the string** in `_VOID_DEFAULT_I18N` (`void/plugins/void_plugin.py`,
   line ~682). Strings are grouped by surface (search, toc, clipboard, etc.).

2. **Override in `mkdocs.yml`:**

   ```yaml
   theme:
     void:
       i18n:
         search_placeholder: "Buscar..."
         toc_title: "En esta pagina"
   ```

3. **Build and verify:**

   ```bash
   mkdocs build --strict
   mkdocs serve
   ```

   Check every chrome surface: search, TOC, keyboard help, notes panel,
   timer, repo popover, footer.

## Adding a new flat alias

If you add a new UI string to the theme:

1. Add the default in `_VOID_DEFAULT_I18N` under the appropriate group.
2. Register a flat alias in `_VOID_I18N_FLAT_ALIASES` (line ~800):

   ```python
   _VOID_I18N_FLAT_ALIASES = {
       # ... existing aliases ...
       "my_new_key": ("group", "child"),
   }
   ```

3. Run `python tools/emit_config_reference.py` to update the reference.
4. Document the key in this page.

## Under the hood

- **Defaults:** `_VOID_DEFAULT_I18N` (line ~682) — 12 nested groups
- **Flat aliases:** `_VOID_I18N_FLAT_ALIASES` (line ~800) — 19 aliases
- **Normalization:** `_normalize_i18n_overrides()` (line ~907) — folds flat
  keys into nested structure
- **Deep merge:** line ~2121 — user overrides merged onto defaults
- **Validation:** `_validate_i18n()` (line ~1652) — rejects unknown keys,
  non-string values
- **JS consumption:** `t(path, fallback)` in `void.js` (line ~203) — reads
  from `__config.translations`

## Accessibility notes

- Translated strings appear in interactive elements (buttons, labels, tooltips).
- Screen readers announce the translated text — ensure translations are
  accurate and grammatically correct for your target language.
- The build aborts on unknown keys, so you'll never have a silently missing
  translation.