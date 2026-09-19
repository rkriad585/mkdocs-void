---
date: 2026-09-07
title: Footnotes
---

# Footnotes

## What it is

Void fully styles [Python-Markdown footnotes](https://python-markdown.github.io/extensions/footnotes/).
Reference footnote markers appear as numbered pills and the definitions render
as a tidy glass card at the end of the article.

## When to use it

Footnotes are for citations, source notes, and asides that would break the
reading flow inline. Prefer them when the extra text belongs at the bottom of
the page, and use inline parentheses or admonitions when the note is essential
to immediate understanding.

## In Markdown

Use the `[^label]` reference in your text and define it with `[^label]: ...`
anywhere below (usually at the end of the document):

```markdown
Void ships with glass morphism[^glass] and a privacy-first[^privacy] promise.

[^glass]: Glass *morphism* uses backdrop blur and translucency.
[^privacy]: No third-party tracking is loaded unless you opt in.
```

## Configuration

The `footnotes` markdown extension is enabled by default in this theme. To
disable it site-wide, remove `- footnotes` from `markdown_extensions` in
`mkdocs.yml`. Styling is always safe to keep — it only applies when footnote
markup is present.

## Live preview / screenshot

Void ships with glass morphism[^glass] and a privacy-first[^privacy] promise.

[^glass]: Glass *morphism* uses backdrop blur and translucency.
[^privacy]: No third-party tracking is loaded unless you opt in.

The `footnotes` markdown extension is enabled by default in this theme, so
footnote markers become `sup` links and the definitions render as a styled list
with a "back to text" link on each entry.

### Multiple references

You can cite the same footnote several times; each marker links to the same
definition[^multi].

```markdown
Repeated reference[^multi] — and again[^multi].

[^multi]: A footnote cited more than once.
```

Repeated reference[^multi] — and again[^multi].

[^multi]: A footnote cited more than once.

## Under the hood

- Markers render as `<sup data-md-footnote>` links back to the definition list
  (`.footnote` output), which Void restyles as a glass card.
- The definition entry carries a "back to text" link so readers can return to
  the exact reference point.
- Because styling keys off the generated `.footnote` markup, it never renders
  on pages without footnotes.

## Accessibility notes

- Markers are real links with a `title`/aria-label pointing to the reference,
  and the back-link returns focus to the original spot — no script needed.
- Numbered pill styling doesn't replace the visible link text, so the target
  is announced to screen readers.