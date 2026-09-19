---
date: 2026-09-07
---

# Code Highlighting

## What it is

Void enhances syntax highlighting with [highlight.js](https://highlightjs.org)
loaded from a CDN. It colorizes code that the base Pygments pipeline leaves
monochrome, respects your light/dark scheme, and keeps the copy button and
per-line anchors working.

## When to use it

Code blocks should be syntax-highlighted on any documentation site — this
component is on by default. Keep it on unless you have a bespoke highlighter;
you can still switch it off per-site with the option below.

## In Markdown

Use standard fenced code blocks; detection is automatic per language:

````markdown
```python
def greet(name):
    print(f"hello {name}")
```
````

highlight.js ships a large set of common languages in its core bundle:

```python
def greet(name):
    print(f"hello {name}")
```

```javascript
function greet(name) {
  console.log(`hello ${name}`);
}
```

```bash
greet() {
  echo "hello $1"
}
```

```rust
fn greet(name: &str) {
    println!("hello {}", name);
}
```

```json
{
  "name": "mkdocs-void",
  "version": "0.1.0"
}
```

## Configuration

Highlighting is controlled by the `void.highlight` theme option:

```yaml
theme:
  void:
    highlight: false
```

Per-component override for the styled layer:

```yaml
theme:
  void:
    components:
      highlighting:
        show: true        # default true
        cdn_url: ""       # empty = theme default CDN
        theme_dark: github-dark
        theme_light: github
```

## Live preview / screenshot

Toggle the palette (light/dark) and the code colors update live to match —
the dark theme is used for the slate scheme and the light theme for light mode.

### Code annotations

Annotate specific lines of a code block with a numbered marker using the
`pymdownx.highlight` guide: end a source line with `# (1)!` (or `// (1)!`,
`-- (1)!`, etc.) and add the numbered legend directly below the block:

```python
import os
cwd = os.getcwd()        # (1)!
```

<ol>
<li>Prints the current working directory.</li>
</ol>

The marker becomes a red pill on that line, and the following `<ol>` becomes a
styled legend — hovering an entry highlights its matching marker. A plain
Markdown ordered list (`1.  ...`) works too when the toolchain emits an `<ol>`
directly after the highlighted block; the raw `<ol>` above is the form that
always renders as a sibling of the code block.

## Under the hood

- highlight.js is requested from the configured CDN only when a `<pre><code>`
  without a `data-highlighted` marker exists on the page.
- Code already processed (marked with `data-highlighted` or `data-no-highlight`)
  is left untouched.
- The `__codelineno` line anchors are preserved, so "copy link to line" keeps
  working.
- The copy button is inserted after highlighting so the `<pre>` wrapper stays
  intact.
- Annotations are applied client-side, so they need no extra Markdown
  extensions. Toggle them off with `theme.void.content.code.annotate: false`.

## Accessibility notes

- Color is not the only cue: monochrome fallback keeps blocks readable, and
  the scheme-aware palette switches to maximize contrast in light and dark.
- The copy button provides labeled text ("Copy"), and the per-line anchors let
  you link directly to a line.