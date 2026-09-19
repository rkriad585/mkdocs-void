---
date: 2026-09-19
title: Compatibility
---

# Compatibility

What versions of MkDocs, Node.js, Python, and browsers Void supports.

## MkDocs

| Version | Status | Notes |
|---------|--------|-------|
| **1.5.3** | ✅ Supported | Minimum supported version. CI-tested. |
| **1.6.1** | ✅ Supported | Current stable. CI-tested. |
| **2.0.0.dev0** | ⚠️ Experimental | CI-tested with `continue-on-error`. May break. |

Void requires the `mkdocs` package and is installed as a theme:

```bash
pip install mkdocs mkdocs-void
```

## Python

| Version | Status |
|---------|--------|
| 3.8 | ✅ Minimum supported |
| 3.9 | ✅ Supported |
| 3.10 | ✅ Supported |
| 3.11 | ✅ Supported (CI default) |
| 3.12 | ✅ Supported |
| 3.13 | ✅ Supported |

## Node.js

| Version | Status | Notes |
|---------|--------|-------|
| 16 | ❌ Not supported | EOL |
| 18 | ✅ Minimum supported | LTS |
| 20 | ✅ Supported | LTS |
| 22 | ✅ Supported | LTS |
| 24 | ✅ Supported | Current |

Node.js is only needed for the CSS build pipeline (`npm run build`). The
theme itself runs purely in Python/Jinja2.

## Browsers

Void uses vanilla ES6+ JavaScript with no transpilation. The CSS uses
standard properties with fallbacks where needed.

| Browser | Minimum version | Notes |
|---------|----------------|-------|
| Chrome | 80+ | Full support |
| Firefox | 80+ | Full support |
| Safari | 14+ | Full support (backdrop-filter needs `-webkit-` prefix) |
| Edge | 80+ | Full support (Chromium-based) |
| Opera | 67+ | Full support (Chromium-based) |
| iOS Safari | 14+ | Full support |
| Chrome Android | 80+ | Full support |
| Samsung Internet | 13+ | Full support |

### Features that degrade gracefully

| Feature | Without JS | Without backdrop-filter | Reduced motion |
|---------|-----------|------------------------|----------------|
| Search | MkDocs built-in | Unaffected | Unaffected |
| SPA navigation | Full page loads | Unaffected | Instant swap (no animation) |
| Color scheme toggle | Server-side default | Unaffected | Unaffected |
| Glass effects | Solid backgrounds | Solid backgrounds | Solid backgrounds |
| Lightbox | Images display normally | Unaffected | Unaffected |
| Focus timer | Unavailable | Unaffected | Unaffected |
| Notes panel | Unavailable | Unaffected | Unaffected |
| Repo popover | Link opens GitHub | Unaffected | Unaffected |
| Toast notifications | Unavailable | Unaffected | Unaffected |
| Reading progress | Bar hidden | Unaffected | Bar hidden |
| Back to top | Button hidden | Unaffected | Scroll is instant |

## CDN dependencies

| Library | Version | Purpose | Loading |
|---------|---------|---------|---------|
| highlight.js | 11.9.0 | Syntax highlighting | Lazy (only on pages with `<code>`) |
| Mermaid.js | 10.9.8 | Diagrams | Lazy (only on pages with `.void-diagram`) |
| KaTeX | 0.16.9 | Math typesetting | Lazy (only on pages with `.arithmatex`) |
| Google Fonts | — | Space Grotesk, Space Mono, Inter | Preconnect + stylesheet |

## CI matrix

The `compat.yml` workflow tests against:

```
MkDocs: 1.5.3, 1.6.1, 2.0.0.dev0
Python: 3.11
OS: ubuntu-latest
```

The test scaffold runs `void new`, `void doctor`, and `mkdocs build --strict`
against each version.

---

[Back to README](../index.md)