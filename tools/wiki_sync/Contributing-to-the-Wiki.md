# Contributing to the Wiki

The wiki is a community-editable companion to the
[canonical docs](https://rkriad585.github.io/mkdocs-void/).

## How to edit

### Directly on GitHub

1. Go to [github.com/rkriad585/mkdocs-void/wiki](https://github.com/rkriad585/mkdocs-void/wiki)
2. Click **Edit** on any page
3. Make your changes and click **Save**

### Via the main repo

Wiki pages are seeded from `tools/wiki_sync/`. To update them:

1. Fork [mkdocs-void](https://github.com/rkriad585/mkdocs-void)
2. Edit files in `tools/wiki_sync/`
3. Open a PR — the wiki sync Action pushes changes on release

## What belongs in the wiki vs. the docs

| Wiki | Docs site |
|------|-----------|
| Quick references | Full guides |
| Community recipes | Official configuration reference |
| FAQ entries | Architecture deep-dives |
| Quick fixes | Component documentation |

## Rules

- **No PLAN files.** Never link or reference `PLAN.md`, `WHY_PLAN.md`,
  `RENAME-PLAN.md`, or `DOCS_WIKI_PLAN.md`.
- **Link back.** Every wiki page should link to the canonical docs for
  detailed information.
- **Keep it current.** The wiki is auto-synced on release — if you edit
  directly, your changes may be overwritten by the next sync.

## Sync behavior

The `wiki-sync.yml` GitHub Action runs on every tag push. It copies the
seed pages from `tools/wiki_sync/` to the wiki. Direct wiki edits are
overwritten by the next sync — so edit the seed files for permanent changes.