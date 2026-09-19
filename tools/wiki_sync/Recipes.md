# Recipes

Common configurations and recipes for mkdocs-void.

## Recipe: Minimal dark docs

```yaml
theme:
  name: void
```

That's it. Void defaults to dark glass, Space Grotesk fonts, and all
components enabled.

## Recipe: Light-only docs

```yaml
theme:
  name: void
  palette:
    - scheme: default
```

## Recipe: Custom accent color

Create `docs/stylesheets/extra.css`:

```css
:root {
  --void-accent: #6c5ce7;
}
```

```yaml
extra_css:
  - stylesheets/extra.css
```

## Recipe: Disable all engagement widgets

```yaml
theme:
  void:
    components:
      feedback:
        show: false
      announcement_bar:
        show: false
      cookie_consent:
        show: false
```

## Recipe: Heavy glass for portfolio sites

```yaml
theme:
  void:
    glass:
      intensity: heavy
```

## Recipe: Custom keyboard shortcuts

```yaml
theme:
  void:
    keyboard:
      shortcuts:
        search:
          key: "Ctrl+K"
        toggle_sidebar:
          key: "Ctrl+B"
      custom:
        - key: "d"
          label: "Toggle dark mode"
          action: "toggle_scheme"
```

## Recipe: GitHub Pages deploy

```yaml
# .github/workflows/docs.yml
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

## Recipe: Netlify deploy

```toml
# netlify.toml
[build]
  command = "pip install mkdocs-void && mkdocs build"
  publish = "site"
```

## Recipe: Read the Docs

```yaml
# .readthedocs.yaml
version: 2
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
python:
  install:
    - method: pip
      path: .
mkdocs:
  configuration: mkdocs.yml
```

## Recipe: Tabbed content

```markdown
=== "Python"

    ```python
    print("Hello!")
    ```

=== "JavaScript"

    ```javascript
    console.log("Hello!")
    ```
```

## Recipe: Task lists

```markdown
- [x] Completed task
- [ ] Pending task
- [ ] Another task
```

## Recipe: Admonitions

```markdown
!!! note "Important"
    This is a note admonition.

!!! warning "Caution"
    This is a warning.

!!! tip
    This is a tip.
```

Full docs: [https://rkriad585.github.io/mkdocs-void/](https://rkriad585.github.io/mkdocs-void/)