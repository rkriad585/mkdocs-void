---
date: 2026-09-07
title: CSS Classes in Markdown
---

# Adding CSS Classes in Markdown

## What it is

Void enables the `attr_list` extension, which lets you **attach component classes (and other attributes) directly to Markdown elements** using a `{.class .another}` suffix. This is the recommended way to style content without writing raw HTML.

## When to use it

Use attribute lists whenever a Markdown element needs a component class — a
card around a paragraph, a rounded image, an accent heading, a styled table.
It keeps the source readable and avoids raw-HTML blocks for the common cases.
For anything more than a couple of classes, plain HTML is fine too.

## In Markdown

!!! note "Enabled by default"
    `attr_list` and `md_in_html` are both enabled in the theme. No configuration required.

### On code blocks

Append `{ .lang .class }` to the opening fence to add classes to the resulting `<pre><code>` — useful for sizing or styling a block:

```py { .void-card .void-p-4 }
print("Hello Void")
```

````markdown
```py { .void-card .void-p-4 }
print("Hello Void")
```
````

The classes land on the `<code>` element, so you can target them in custom CSS.

### On images

```markdown
![alt](img.png){ .void-img-round width="140" }
```

Both classes and other attributes (`width`, `height`, `loading`) are applied.

```
![Round](img.png){ .void-img-round width="140" }
![Ghost](img.png){ .void-img-ghost }
![Banner](img.png){ .void-image--banner }
```

### On headings

```markdown
## Installation { .void-accent }
```

```html
<h2 class="void-accent">Installation</h2>
```

### On any block element

Attach classes to paragraphs, lists, blockquotes, and more:

```markdown
> A highlighted quote { .void-card }
```

```
| Head | Head |
|------|------|
| A    | B    | { .void-table }
```

### Combining with your own classes

You can attach your own classes alongside the theme's. Any CSS you add via `extra_css` will apply:

```markdown
```yaml { .my-custom-block .language-yaml }
key: value
```
```

## Configuration

`attr_list` is toggled through `pymdownx` or the theme's defaults — both it and
`md_in_html` ship enabled in the theme, so there is nothing to configure for
vanilla use. Both are enabled by default in this theme.

## Live preview / screenshot

Text that lets you verify the classes attach in the rendered page:

> A highlighted quote { .void-card }

```markdown
> A highlighted quote { .void-card }
```

Combined classes on an image (round crop + fixed width):

![Round](https://raw.githubusercontent.com/rkriad585/mkdocs-void/main/docs/assets/images/logo.svg){ .void-img-round width="140" }

## Under the hood

`attr_list` is an official Python-Markdown extension. The syntax is `{...}` immediately after the element (no blank line before it). Available attributes include `class`, `id`, `width`, `height`, `title`, and more. Because both `attr_list` and `md_in_html` are active, you can mix raw HTML and Markdown attributes freely.

For full details, see the [Python-Markdown attr_list docs](https://python-markdown.github.io/extensions/attr_list/).

## Accessibility notes

- Attribute-list classes are presentational; they add no semantics on their own.
  `.void-accent`, `.void-card`, and sizing utilities don't change the element's
  role or name, so screen-reader output stays identical to the plain element.
- Keep `alt` text on images meaningful even when `width`/`height` attributes
  size them down.