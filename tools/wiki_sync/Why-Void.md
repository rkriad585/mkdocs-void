# Why Void

Void is a dark-first, glassmorphism MkDocs theme with vanilla JS, zero
dependencies, and a single-file architecture.

## Why choose Void over Material or Read the Docs?

| | Void | Material | Read the Docs |
|---|---|---|---|
| **Default look** | Dark glass, ready out of the box | Light, requires config for dark | Light, minimal |
| **Dependencies** | Zero — vanilla JS | Some (instant loading, etc.) | Some |
| **Glass effects** | Built-in, configurable | Not built-in | Not built-in |
| **Keyboard shortcuts** | `/` search, `?` help, 16+ bindings | Limited | Limited |
| **Focus timer** | Built-in | Not built-in | Not built-in |
| **Notes panel** | Built-in | Not built-in | Not built-in |
| **SPA navigation** | Built-in prefetch + scroll restore | Built-in | Not built-in |
| **Config builder** | Visual YAML editor | Not built-in | Not built-in |
| **Action cluster** | Floating menu with customizable actions | Not built-in | Not built-in |

## Design philosophy

1. **Dark-first** — the default is a dark glass UI, not a light theme with
   a dark mode bolted on.
2. **Single-file JS** — all behavior in one `void.js` IIFE, no bundler, no
   framework.
3. **Config-driven** — every feature toggles via `mkdocs.yml`, no code
   editing required.
4. **Progressive enhancement** — works without JS, degrades gracefully
   without backdrop-filter.

Full docs: [https://rkriad585.github.io/mkdocs-void/](https://rkriad585.github.io/mkdocs-void/)