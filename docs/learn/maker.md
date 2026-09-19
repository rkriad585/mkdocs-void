---
date: 2026-09-19
title: "Level 2 — Maker"
---

# Level 2 — Maker

**Time:** ~1–2 hours

You'll write real documentation pages, use components, change a design token,
and deploy to GitHub Pages.

## What you'll learn

- How to write docs with admonitions, tabs, and task lists
- How to use the component system
- How to change a design token and see it apply
- How to deploy to GitHub Pages

## Prerequisites

- Completed [Level 1 — Explorer](explorer.md)
- A GitHub account
- Git installed

## Step 1 — Write a component page

Create `docs/guide.md`:

```markdown
---
date: 2026-09-19
title: My Guide
---

# My Guide

!!! note "Tip"
    Admonitions are built in. Use `!!! note`, `!!! warning`, `!!! tip`, etc.

## Tabs

=== "Python"

    ```python
    print("Hello from Void!")
    ```

=== "JavaScript"

    ```javascript
    console.log("Hello from Void!")
    ```

## Task lists

- [x] Install Void
- [x] Scaffold a project
- [ ] Write documentation
- [ ] Deploy to GitHub Pages
```

Run `mkdocs serve` and check that admonitions, tabs, and task lists all
render correctly.

## Step 2 — Use the notes panel

1. Press `Ctrl+Shift+N` to open the notes panel.
2. Click "Add note" and write a note about your page.
3. The note is saved in `localStorage` and persists across reloads.

## Step 3 — Change a design token

Create `docs/stylesheets/extra.css`:

```css
:root {
  --void-accent: #00ff88;
}
```

Add it to `mkdocs.yml`:

```yaml
extra_css:
  - stylesheets/extra.css
```

Reload the site. The accent color (used for links, active states, and the
progress bar) should now be green.

## Step 4 — Deploy to GitHub Pages

1. **Create a GitHub repo** and push your project:

   ```bash
   git init
   git add .
   git commit -m "Initial docs"
   git remote add origin https://github.com/your-username/my-docs.git
   git push -u origin main
   ```

2. **Set the `site_url`** in `mkdocs.yml`:

   ```yaml
   site_url: https://your-username.github.io/my-docs/
   ```

3. **Add a deploy workflow.** Create `.github/workflows/docs.yml`:

   ```yaml
   name: Deploy docs
   on:
     push:
       branches: [main]
   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-python@v5
           with:
             python-version: "3.11"
         - run: pip install mkdocs-void
         - run: mkdocs build --strict
         - uses: peaceiris/actions-gh-pages@v4
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./site
   ```

4. **Push and check** the Actions tab — the site deploys automatically.

## Verify you got it

- [ ] A live site at `mkdocs serve` with admonitions, tabs, and task lists
- [ ] A design token change visible in the browser
- [ ] Notes panel opens with `Ctrl+Shift+N`
- [ ] A deployed site on GitHub Pages

## Next level

Ready to customize the theme deeply? Continue to
[Level 3 — Customizer](customizer.md).

---

[Back to Learn](index.md)