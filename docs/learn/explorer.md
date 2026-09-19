---
date: 2026-09-19
title: "Level 1 — Explorer"
---

# Level 1 — Explorer

**Time:** ~30 minutes

You'll go from "what is this?" to a running local preview with the docs
tour completed.

## What you'll learn

- What Void is and why it exists
- How to install it
- How to scaffold a project
- How to serve the docs locally
- The main features at a glance

## Prerequisites

- Python 3.8+
- pip

## Step 1 — Install

```bash
pip install mkdocs-void
```

Verify:

```bash
void --version
```

## Step 2 — Scaffold a project

```bash
void new my-docs
cd my-docs
```

This creates a ready-to-go project with `mkdocs.yml`, a `docs/` folder,
and all the defaults wired up.

## Step 3 — Serve

```bash
mkdocs serve
```

Open `http://127.0.0.1:8000` in your browser.

## Step 4 — Tour the features

While the site is running, try these:

1. **Dark/light toggle** — click the moon/sun icon in the header
2. **Search** — press `/` to open the full-screen search
3. **Keyboard shortcuts** — press `?` to see all available bindings
4. **Sidebar** — click sections to expand/collapse
5. **Code copy** — hover a code block and click the copy button
6. **Tabs** — click between tabbed content sections
7. **Reading progress** — scroll down and watch the bar at the top

## Step 5 — Explore the config

Open `mkdocs.yml` and look at the `theme.void` section. Every feature you
just saw is controlled from here. You can:

- Change the color scheme
- Toggle components on/off
- Adjust glass intensity
- Set the repo URL

## Verify you got it

- [ ] `void --version` prints a version number
- [ ] `mkdocs serve` starts without errors
- [ ] The site opens at `http://127.0.0.1:8000`
- [ ] You can toggle dark/light mode
- [ ] You can open search with `/`
- [ ] You can see the keyboard shortcut panel with `?`

## Next level

Ready to write your own docs and deploy? Continue to
[Level 2 — Maker](maker.md).

---

[Back to Learn](index.md)