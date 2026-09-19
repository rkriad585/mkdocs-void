---
date: 2026-09-19
title: Persistence
---

# Persistence

## What it is

Void stores reader preferences and state in `localStorage` under the `void-`
prefix. Every key is per-browser, per-site, and never sent to a server.
This page documents every key, what it stores, and its default lifetime.

## When to use it

Persistence is always on. The theme reads these keys on boot to restore
the reader's previous state — color scheme, collapsed sidebar, scroll
position, and so on. Understanding the keys helps with debugging and with
clearing stale data.

## How it works

All reads and writes go through `storageGet(key)` / `storageSet(key, value)`,
which prepend `void-` to the key name. A few keys (like `void-scroll-pos`)
are written directly to `localStorage` for performance.

## localStorage keys

| Key | Written by | What it stores | Lifetime |
|-----|-----------|----------------|----------|
| `void-color-scheme` | `applyColorScheme()` | Current palette scheme (`"default"`, `"slate"`, …) | Persistent |
| `void-session` | `sessionMutate()` | JSON blob: `{ lastPage, lastAt, navCollapsed, search, search_history }` | Session |
| `void-scroll-pos` | `saveCurrentScroll()` | `pageURL → { y, x, at }` scroll map | Persistent |
| `void-ui-reading` | `readingModeSet()` | Reading mode `"1"`/`"0"` | Persistent (when `reading_mode.persisted`) |
| `void-ui-sidebar` | Sidebar toggle | Nav sidebar hidden `"1"`/`"0"` | Persistent (when `persisted`) |
| `void-ui-toc` | TOC toggle | TOC hidden `"1"`/`"0"` | Persistent (when `persisted`) |
| `void-ui-notes` | `notesSetOpen()` | Notes panel open `"1"`/`"0"` | Persistent |
| `void-notes` | `notesAddComposer()` | JSON array of notes `{ id, url, text, note, color, ts }` | 3 days (TTL) |
| `void-note-did-apply-<id>` | `notesReapply()` | `"1"` flag: highlight applied for that note | Persistent |
| `void-task.<path>.<n>` | Task list checkbox | `"1"`/`"0"` checkbox state | Persistent |
| `void-tabs.<path>.<set>` | Tab switcher | Last active tab index per tabbed-set | Persistent |
| `void-focus-timer` | `focusTimerRestore()` | `{ remaining, running, updatedAt }` timer session | Persistent (when `timer.persist`) |
| `void-focus-timer-settings` | `focusTimerApplySettings()` | Reader timer overrides `{ default_minutes, ... }` | Persistent |
| `void-consent` | Cookie consent | `"accepted"` / `"declined"` | Persistent |
| `void-announcement-dismissed-<text>` | Announcement bar | `"1"` = dismissed for that exact text | Persistent |
| `void-cache-repo-<owner>/<name>` | `repoPopover` | `{ ts, data }` GitHub API cache | 1 hour (TTL) |
| `void-glass-intensity` | Glass restore | Glass intensity value → `data-md-void-glass` | Persistent |

### Session-only (inside `void-session`)

| Field | What it stores |
|-------|----------------|
| `lastPage` | Last visited page URL |
| `lastAt` | Timestamp of last visit |
| `navCollapsed` | Array of collapsed sidebar section IDs |
| `search` | Last search query |
| `search_history` | Last 5 search queries |

## Configuration

Most persistence is opt-in or opt-out per feature:

```yaml
theme:
  void:
    reading_mode:
      persisted: true                # Remember reading mode (default true)
    timer:
      persist: true                  # Remember timer state (default true)
    content:
      task_lists:
        persist_state: true          # Remember checkbox states (default true)
    keyboard:
      shortcuts:
        toggle_sidebar:
          persisted: true            # Remember sidebar state (default true)
        toggle_toc:
          persisted: true            # Remember TOC state (default true)
    notes_ttl: 259200000             # Notes retention in ms (default 3 days)
```

## Under the hood

- **File:** `void.js` — `storageGet()`/`storageSet()` (line ~16), `sessionGet()`/`sessionMutate()` (line ~72)
- **Prefix:** all keys use `void-` except `void-scroll-pos` (written directly)
- **TTL:** `notes` uses a 3-day TTL (`259200000` ms); `repo-popover` uses a
  1-hour TTL (`3600000` ms). Expired entries are removed on next read.
- **Scope:** all keys are per-origin — changing `site_url` or deploying to a
  different domain starts fresh.

## Accessibility notes

- Persistence is transparent — readers never see the stored data directly.
- Clearing site data (or specific `void-*` keys) resets all state without
  breaking the site.
- The notes TTL auto-purges old entries, so the store never grows unbounded.