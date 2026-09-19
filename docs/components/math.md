---
date: 2026-09-07
title: Math
---

# Math (KaTeX)

## What it is

Void renders mathematical notation with **KaTeX**, loaded lazily from a CDN only when a page contains math. It integrates with `pymdownx.arithmatex`, which is enabled in the theme's `mkdocs.yml`.

## When to use it

Use math for formulas, equations, and notation on pages where they're the
content — API docs, algorithms, scientific prose. On prose-heavy pages, inline
math ($x^2$) keeps notation compact; block math is for equations worth standing
on their own line.

## In Markdown

Use single dollar signs for inline math:

```markdown
The quadratic formula **$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$** solves $ax^2 + bx + c = 0$.
```

The quadratic formula **$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$** solves $ax^2 + bx + c = 0$.

Use double dollar signs (or a `$$ ... $$` block) for display math:

```markdown
$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$
```

$$
\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}
$$

## Configuration

Math is enabled by default. To disable it entirely set `extra.void_math: false`
in `mkdocs.yml`; to only hide the loader for a single component category use
`theme.void.components.math.show: false`:

```yaml
# mkdocs.yml — disable math globally
extra:
  void_math: false
```

```yaml
theme:
  void:
    components:
      math:
        show: true        # default true
        cdn_url: ""       # empty = theme default
        cdn_css_url: ""
```

## Live preview / screenshot

### Aligned equations

$$
\begin{aligned}
E &= mc^2 \\
F &= ma
\end{aligned}
$$

### Matrices

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\cdot
\begin{pmatrix}
x \\
y
\end{pmatrix}
=
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

## Under the hood

- Math is loaded only when a `.arithmatex` element exists on the page, so pages
  without math never fetch KaTeX.
- The KaTeX resources are pinned to `katex@0.16.9` (CSS + JS) from `jsdelivr`.

## Accessibility notes

- KaTeX renders math as text-plus-CSS where possible, keeping content
  selectable and screen-reader accessible; add an aria-label for complex
  expressions when it aids comprehension.
- Avoid math as the only carrier of a result — restate the implication in prose.