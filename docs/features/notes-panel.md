---
date: 2026-09-19
title: Notes Panel
---

# Notes Panel

## What it is

A browser-local sticky-note layer. Open the panel with `Ctrl+Shift+N`, add
notes with a color and a quoted anchor, and export them as Markdown or JSON.
Notes persist in `localStorage` for 3 days (configurable) and are global —
they appear on every page.

## When to use it

Use the notes panel for personal annotations while reading — questions to
revisit, reminders, or quick captures. Notes are per-reader (never sent to
a server), so they're ideal for private study or temporary context.

## How it works

The notes panel is a sidebar overlay that slides in from the left. Each note
has a color, a quoted anchor (the text you selected when you created it), and
a comment. Notes are stored as a JSON array in `void-notes` and annotated in
the article as `<mark class="void-note__hl">` elements.

### Adding a note

1. Open the panel (`Ctrl+Shift+N`).
2. Press **+ Add note**.
3. Select text in the article (optional — the anchor is captured automatically).
4. Pick a color, type your note, press **Save**.

### Exporting

- **Export .md** — downloads `void-notes.md` with headings, quotes, and metadata.
- **Export .json** — downloads `void-notes.json` for backup or migration.

### Keyboard shortcuts

| Key | Action |
|-----|--------|
| `Ctrl+Shift+N` | Toggle the notes panel |
| `Esc` | Close the panel (or cancel the composer) |
| `Tab` | Cycle through panel controls (focus trap) |

## Configuration

```yaml
theme:
  void:
    notes:
      show: true                        # Render the notes feature (default true)
    notes_ttl: 259200000                # Retention in ms (default 3 days = 259200000)
```

The keyboard shortcut is remappable under `theme.void.keyboard.shortcuts.toggle_notes`.

## Under the hood

- **File:** `void.js` — `initNotes(config)` (line ~3728),
  `notesCompose(existing)` (line ~3422), `notesAddComposer()` (line ~3517),
  `notesRefreshPanel()` (line ~3610), `notesDelete()` (line ~3676),
  `notesExportMarkdown()` (line ~3702), `notesExportJson()` (line ~3716)
- **localStorage keys:**
  - `void-notes` — JSON array of `{ id, url, text, note, color, ts }`
  - `void-ui-notes` — `"1"`/`"0"` panel open state
  - `void-note-did-apply-<id>` — `"1"` flag: highlight applied for that note
- **Classes:** `.void-notes-btn`, `.void-notes-panel` (id `void-notes-panel`),
  `.void-note__item`, `.void-note__composer`, `.void-note__color`,
  `.void-note__save`, `.void-note__cancel`, `.void-note__edit`,
  `.void-note__delete`, `.void-note__hl` (highlight marks)
- **TTL:** notes older than `notes_ttl` ms are purged on panel open and on
  every `notesRefreshPanel()` call.
- **Global:** notes are not scoped to a page — the same set appears everywhere.

## Accessibility notes

- The panel is a keyboard-openable overlay with focusable controls (add,
  edit, delete, export) and plain-text labels.
- `Esc` closes the panel and returns focus to the trigger.
- Highlight marks use `<mark>` with `aria-hidden="true"` — they're visual
  only; the note text is in the panel.
- Color is a hint, not the only signal — note text and the edit/delete
  buttons are always readable.