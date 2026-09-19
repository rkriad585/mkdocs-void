---
date: 2026-09-19
title: Repo Popover
---

# Repo Popover

## What it is

Press `Ctrl+Shift+G` (or hover the repo icon in the header) to open a card
showing GitHub project data: stars, forks, latest commit, language, license,
and more. The data is fetched from the GitHub API, cached for 1 hour, and
rendered as a glass panel that persists until you dismiss it.

## When to use it

The repo popover is a quick-glance project dashboard for readers who want
to check the project's health without leaving the docs. It's especially
useful on docs-heavy sites where the GitHub repo link is buried in the header.

## How it works

When the header contains a `.void-header__repo` link (from `repo_url` in
`mkdocs.yml`), `initRepoPopover()` binds hover/click/focus handlers that
fetch four GitHub API endpoints in parallel:

1. `/repos/:owner/:name` — stars, forks, watchers, language, license, etc.
2. `/tags?per_page=1` — latest tag
3. `/commits?per_page=1` — latest commit (total from `Link` header)
4. `/users/:owner` — owner bio, followers, public repos, location

The results are cached in `void-cache-repo-<owner>/<name>` with a 1-hour TTL.

### Data fields

| Field | Source |
|-------|--------|
| description | `/repos/:owner/:name` |
| owner_bio | `/users/:owner` |
| author | `/repos/:owner/:name` → `owner.login` |
| followers | `/users/:owner` → `followers` |
| public_repos | `/users/:owner` → `public_repos` |
| location | `/users/:owner` → `location` |
| stars | `/repos/:owner/:name` → `stargazers_count` |
| watchers | `/repos/:owner/:name` → `subscribers_count` |
| forks | `/repos/:owner/:name` → `forks_count` |
| open_issues | `/repos/:owner/:name` → `open_issues_count` |
| language | `/repos/:owner/:name` → `language` |
| license | `/repos/:owner/:name` → `license.spdx_id` |
| default_branch | `/repos/:owner/:name` → `default_branch` |
| commits | Derived from `Link` header on `/commits` |
| tags | `/tags?per_page=1` → first tag name |
| latest_commit | `/commits?per_page=1` → `sha` (short) |
| commit_msg | `/commits?per_page=1` → `commit.message` |
| created | `/repos/:owner/:name` → `created_at` |
| updated | `/repos/:owner/:name` → `updated_at` |
| pushed | `/repos/:owner/:name` → `pushed_at` |

## Configuration

```yaml
theme:
  void:
    components:
      repo_popover:
        show: true                      # Enable the popover (default true)
        fields:                         # Which fields to render (default: all)
          - description
          - owner_bio
          - author
          - followers
          - public_repos
          - location
          - stars
          - watchers
          - forks
          - open_issues
          - language
          - license
          - default_branch
          - commits
          - tags
          - latest_commit
          - commit_msg
          - created
          - updated
          - pushed
```

Opt out of specific sections by listing only the ones you want. The shortcut
is remappable under `theme.void.keyboard.shortcuts.toggle_repo_popover`.

## Under the hood

- **File:** `void.js` — `initRepoPopover(config)` (line ~4809),
  `openRepoLink()` (line ~5086), `toggleRepoPopover()` (line ~5096)
- **Guard:** only renders when `repo_url` points to a GitHub host; for
  non-GitHub repos, `Ctrl+Shift+G` opens the repo link in a new tab.
- **Cache:** `void-cache-repo-<owner>/<name>` — 1-hour TTL, generic
  `cacheGet`/`cacheSet` helpers.
- **Avatar:** resolved from `https://github.com/<owner>.png?size=80` — no
  rate limit, never stale.
- **Trigger:** opens on `mouseenter`, `pointerenter`, `focus`, `click`, and
  Enter/Space. Closes on `mouseleave`, `focusout`, outside pointer, or
  Escape. No auto-close timer — the card persists until dismissed.

## Accessibility notes

- The popover is a `role="tooltip"` panel with an `aria-label` on the trigger.
- `Escape` closes the popover and returns focus to the trigger.
- Focus is trapped inside the popover while it's open.
- Data loading failures render a graceful error message ("Unable to load
  repo data") — the popover never blocks the page.