---
date: 2026-09-07
---

# Tabs

## What it is

Void styles `pymdownx.tabbed` content with a glass-styled tab strip that
follows the theme accent. Styling supports up to 10 tabs and adds keyboard
navigation via a small script.

## When to use it

Use tabs to group alternate views of the same thing — the same snippet in
different languages, platform-specific steps, light/dark illustrations. Keep
each tab self-contained; don't split a single linear explanation across tabs.

## In Markdown

Use the `=== "Label"` syntax inside a tab list:

````markdown
=== "Python"
    ```python
    print("hello")
    ```

=== "JavaScript"
    ```js
    console.log("hello");
    ```

=== "Bash"
    ```bash
    echo "hello"
    ```
````

## Configuration

Tabs require the `pymdownx.tabbed` extension (enabled in the theme's
`mkdocs.yml`); no per-site configuration is needed beyond that.

## Live preview / screenshot

### Example — three tabs

=== "Python"
    ```python
    def greet(name):
        print("hello " + name)
    ```

=== "JavaScript"
    ```js
    function greet(name) {
      console.log("hello " + name)
    }
    ```

=== "Bash"
    ```bash
    greet() {
      echo "hello $1"
    }
    ```

### Example — many tabs (8)

=== "Tab 1"

    Content one.

=== "Tab 2"

    Content two.

=== "Tab 3"

    Content three.

=== "Tab 4"

    Content four.

=== "Tab 5"

    Content five.

=== "Tab 6"

    Content six.

=== "Tab 7"

    Content seven.

=== "Tab 8"

    Content eight.

## Under the hood

- Tab groups render `.void-tabs` with `.void-tabs__item` labels; the active one
  carries the accent underline.
- A small script adds roving-tabindex + arrow-key navigation after the
  `pymdownx.tabbed` markup is emitted, keeping the native structure intact.

## Accessibility notes

- Use `Tab` to focus a tab label, then `ArrowLeft` / `ArrowRight` to switch
  tabs — the active tab is indicated with the accent underline.
- Panels stay standard tabbed content: each tab's content is contained and
  reachable by keyboard, and the current selection is not conveyed by color
  alone (underline + focus position).