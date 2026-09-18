---
date: 2026-09-18
title: Why Void
---

# Why Void

> Made by the anti-default.

Void is the MkDocs theme you pick when your documentation should look like
*your brand* — not the same indigo sidebar everyone else ships. It blends the
translucent depth of **Glass** with the industrial minimalism of **NothingOS**:
a pure black canvas, dot-matrix texture, and Nothing Red accents, all driven
from a single `mkdocs.yml`.

The whole pitch fits in one sentence:

> Give a developer a distinctive, fast, privacy-first docs site in under two
> minutes — purely from `mkdocs.yml` — without a single line of custom CSS.

## The three pillars

Every decision in Void serves these three commitments:

1. **Distinctive by default** — a zero-config build looks intentional and
   unique. Glass morphism, the NothingOS black canvas, dot-matrix, and Nothing
   Red are the visual language that flat, indigo Material clones cannot copy
   without forking.
2. **Fast + app-like** — SPA-style navigation, a service-worker cache, and a
   tiny footprint. Pages feel like a native app, not a document dump.
3. **Private by default** — no tracking pixels, no mandatory CDN, no analytics
   injected without your say-so. Configuration-first, self-host-friendly.

!!! note
    These are not aspirational. Each pillar maps to shipped, verified code in
    this repository — the design system, the SPA + service worker, and the
    config-driven asset loading. See [Architecture](architecture.md) for the
    internals and [Performance](performance.md) for the page-weight budget.

## Why not Material?

Material for MkDocs is the 800-pound gorilla — and it has **stopped evolving**.
On 2025-11-06 the project formally entered **maintenance mode**: critical bug
and security fixes will continue until November 2026, but no new features will
ship. The 9.7.0 release (2025-11-11) folded every previously paid "Insiders"
feature into the MIT edition, and the team's new feature work moved to a
successor project, **Zensical**.

Void is the actively-maintained alternative in the same ecosystem. It is not a
Material clone — it is a different design language that prioritizes three
things Material was never built around: a distinctive visual identity, speed,
and privacy.

The honest comparison (dated 2026-09-18):

| Capability | Void | Material for MkDocs |
|-----------|--------|---------------------|
| Design language | Glass + NothingOS (distinctive) | Material Design (universal, bland) |
| Actively maintained | Yes — this repo | Maintenance mode; new features frozen |
| Zero-config distinctive look | Yes | No (all look alike) |
| SPA navigation | Yes | Yes |
| Service-worker caching | Yes | Yes |
| Privacy-first defaults | Yes — no trackers, self-hostable | CDN-dependent |
| Config-first custom CSS | Yes — token overrides | Yes |
| Full config from one YAML | Yes | Yes |

*Sources — [maintenance-mode announcement](https://github.com/squidfunk/mkdocs-material/issues/8523)
(2025-11-06), [release notes](https://github.com/squidfunk/mkdocs-material/releases)
(9.7.0 folded Insiders into MIT; fixes committed through November 2026),
[project repository](https://github.com/squidfunk/mkdocs-material).*

Void wins on the two axes developers actually feel: **identity** and
**maintenance pace**.

## The anti-default

Every "default" docs theme pushes you toward the same indigo header, the same
sidebar, the same flat surfaces. Void inverts that assumption: the defaults
are the showpiece. Turn on the theme and you already have glass panels, a
dot-matrix canvas, Nothing Red accents, dark/light schemes, full-screen search,
and reading mode — no custom CSS, no theming homework.

If you want your docs to be remembered, start from the theme that forgot to be
boring.

## Honest limitations

No theme is free of trade-offs, and Void documents its own:

- **No JavaScript.** The site still renders fully server-side — every page,
  heading, and plain navigation link works — because MkDocs ships static HTML.
  The *app layer* is inactive without JS: full-screen search, SPA transitions,
  reading mode, palette toggle, focus timer, notes, and the service worker all
  need a browser that runs scripts.
- **`backdrop-filter` support.** The glass blur needs a modern Chromium,
  Firefox, or Safari/WebKit engine. On engines without it, glass surfaces fall
  back to a semi-transparent flat panel — the layout, colors, and hierarchy are
  unchanged, only the blur is lost.
- **GitHub rate limits on the repo popover.** The repo popover reads the public
  GitHub REST API unauthenticated and caches results. Unauthenticated requests
  share an IP-based rate budget, so during bursts the popover can serve stale or
  delayed data — it degrades gracefully to a plain link either way.
- **Search index size.** Search runs fully client-side, so a very large
  documentation set (tens of thousands of pages) will slow the index build and
  the query path. For such sites, pair Void with an external search provider.

---

[Back to README](index.md)