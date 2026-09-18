# DOCS_WIKI_PLAN.md — the definitive documentation & GitHub Wiki plan for mkdocs-void

> The single place that plans, end-to-end, **everything a developer needs to
> know** about Void: *why use it, how to use it, how to configure it, how it
> works inside, how to extend it, and how the community documents it* — so a
> reader can go from "what is this?" to "deployed, branded, customized" without
> ever leaving the docs.
>
> Companion files: `PLAN.md` (feature/config-surface roadmap), `WHY_PLAN.md`
> (strategy: why developers choose Void). `RENAME-PLAN.md` is a **historical
> artifact** of the `mkdocs-neoabs` → `mkdocs-void` rename — it is kept for
> record only. The **Mandatory Working Rules below bind every phase in this
> file** — they are the same rules as in `PLAN.md` and `WHY_PLAN.md`.

---

## ⚠️ Mandatory Working Rules (READ BEFORE STARTING ANY WORK)

> These rules apply to **every** phase in this plan. Breaking any of them is a
> defect and must be treated as one. Re-read them before finishing each phase.

1. **Don't remove any element.** Never delete existing HTML elements, Jinja
   blocks, CSS rules/classes, IDs, or markup that the theme already renders.
   Extend them or hide them via config — never strip them out.
2. **Don't remove any feature.** Every feature documented in the README, the
   `docs/` folder, or present in the theme today must keep working after any
   phase. Enabling/disabling goes through the existing config defaults; nothing
   may silently disappear.
3. **Don't remove any function.** Never delete or rename an existing JavaScript
   function, Python method, plugin hook, or init entry point. New code may wrap
   or extend; existing call sites stay intact and callable.
4. **Don't make any typo.** Verify every identifier — config keys, CSS custom
   property names, function names, class names, file paths, and every doc page
   name/link — against the actual source before and after every edit. A typo in
   a config key, class, asset URL, or doc link is a bug.
5. **Don't touch any code outside the phase's topic.** Each phase lists the
   files it may modify (mostly `docs/`, `README.md`, `mkdocs.yml` nav, `tools/`
   doc utilities, and the wiki). You must not edit any file outside that list.
   If a change appears to require an out-of-scope file, stop and add that file
   to the phase's list first.
6. **Don't miss any feature in a phase.** Each phase defines a **complete** set
   of pages, config keys, and behaviors. Implement them **all**. A phase is not
   done until every listed item has a working, accurate doc and every task in
   that phase is checked off.
7. **One truth, generated.** Hand-written pages never duplicate the config
   reference — always include (or generate from) the plugin's canonical tables
   (`_VOID_TOKEN_MAP`, `_void_defaults` in `void/plugins/void_plugin.py`, and
   `tools/emit_config_reference.py`). Never document a key that has no working
   consumer.
8. **Everything stays enabled/active by default.** All new features default to
   ON (or keep their previous default value). Never ship a config default of
   `false` unless the phase explicitly says otherwise.
9. **Verification is part of the phase.** After each phase: `npm run build`,
   `mkdocs build --strict`, `npm test`, `tools/check_docs.py`, and the relevant
   harnesses must all pass before moving on. No phase is complete without a
   green build, green tests, and green doc checks.
10. **Never "fix" a symptom by deleting the feature.** If a feature or doc
    misbehaves, fix the bug. Do not disable, hide, remove, or silently rewrite a
    feature to make checks pass.
11. **Docs & READMEs never link plan files.** No `docs/**` page, no README
    (root `README.md` or any README you edit), and no wiki page may link to,
    embed, or reference `PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, or
    `DOCS_WIKI_PLAN.md`. These are planning artifacts — never user-facing
    content. The docs and READMEs must stand alone; planning references live
    only inside this file and its companions. This rule is repeated as a
    checklist line in **every** phase below.

---

## Table of contents

- [1. Purpose & targets](#1-purpose--targets)
- [2. Documentation philosophy & quality bar](#2-documentation-philosophy--quality-bar)
- [3. Content inventory — every single thing the docs must explain](#3-content-inventory--every-single-thing-the-docs-must-explain)
- [4. Target documentation map (nav of the finished site)](#4-target-documentation-map-nav-of-the-finished-site)
- [5. GitHub Wiki plan](#5-github-wiki-plan)
- [6. Phases](#6-phases)
  - [Phase 1 — Audit & doc health](#phase-1--audit--doc-health)
  - [Phase 2 — Why & onboarding](#phase-2--why--onboarding)
  - [Phase 3 — Configuration Bible](#phase-3--configuration-bible)
  - [Phase 4 — Design system & components deep-dive](#phase-4--design-system--components-deep-dive)
  - [Phase 5 — Features & behavior index](#phase-5--features--behavior-index)
  - [Phase 6 — Developer docs & learning curve](#phase-6--developer-docs--learning-curve)
  - [Phase 7 — GitHub Wiki](#phase-7--github-wiki)
  - [Phase 8 — AI-readable, PWA & i18n](#phase-8--ai-readable-pwa--i18n)
  - [Phase 9 — Quality, CI & maintenance](#phase-9--quality-ci--maintenance)
- [7. Definition of done](#7-definition-of-done)
- [8. Risks & constraints](#8-risks--constraints)
- [9. Supporting plans & artifacts](#9-supporting-plans--artifacts)

---

## 1. Purpose & targets

**Goal:** make Void documentation so complete and pleasant that "I read the
docs" is the fastest path from zero to a live, customized site — and so
well-structured that contributors and maintainers never fight stale content.

**Two surfaces, one truth:**

| Surface | Where | Role |
|---|---|---|
| **Docs site** | `docs/` + `mkdocs.yml` (built by the theme itself) | Canonical, version-pinned, always-current reference & tutorials |
| **GitHub Wiki** | `rkriad585/mkdocs-void.wiki` | Community space: recipes, translated guides, informal notes, release notes, screenshots gallery |

**Audience tiers** (every page is written to exactly one tier):

1. **User** — the developer adopting Void for their own docs.
2. **Contributor** — someone patching the theme (Python/JS/SCSS/docs).
3. **Maintainer** — the person shipping releases, screenshots, and CI.

**Depth guarantee:** for every config key there is (a) a definition, (b) a
default, (c) a worked example, and (d) a screenshot or live demo where possible.
No key is documented from memory — it is generated from the plugin where we
can, cross-checked against the source where we can't.

**Current state (baseline for every phase):** the theme has shipped through
**0.2.2** on PyPI (`mkdocs-void`), the docs site is live at
`https://rkriad585.github.io/mkdocs-void`, and most pages planned below already
exist. Phases in §6 mark each item **[shipped]** or **[gap]** so new work is
always the delta, never a rewrite of the past.

---

## 2. Documentation philosophy & quality bar

1. **Generated > hand-written.** The config reference mirrors
   `void/plugins/void_plugin.py` (`_VOID_TOKEN_MAP`, `_void_defaults`) and is
   emitted by `tools/emit_config_reference.py` into `docs/_config_ref.generated.md`,
   which `docs/getting-started/configuration.md` pulls in with a snippets
   include. Humans never retype truth.
2. **Every example is tested.** Doc snippets must build. The recipe/integration
   assertions (`mkdocs-git-revision-date-localized-plugin`, `mkdocs-print-site`,
   `mkdocs-table-reader`, `mkdocs-section-index`, `mkdocs-awesome-pages`) are
   proven in a scratch MkDocs project in CI; a snippet that breaks the build is
   a bug.
3. **No dead config.** A documented key without a working consumer is a bug.
4. **Screenshots for everything visual.** `tools/screenshots_gen.py` regenerates
   the gallery (17 shots in `Screenshots/`); `docs/screenshots.md` must never
   reference a missing file.
5. **One level deeper than competitors.** Where Material shows *that* something
   exists, Void docs show *why it exists, when to use it, what happens under the
   hood, and how it degrades* (offline, no-JS, reduced-motion, no
   `backdrop-filter`).
6. **Searchable and AI/LLM-friendly.** Robust page titles, one H1 per page,
   JSON-LD + social-card og:image per page, and the AI-readable mode already
   ships on this site: every page also has a watermarked markdown mirror, a
   root `llms.txt`, a concatenated `llms-full.txt`, and PWA manifest
   (`manifest.webmanifest`).
7. **Docs stand alone.** Docs and READMEs never point at planning artifacts
   (Rule 11). If a page needs roadmap context it links to another doc page or
   the changelog — never to a PLAN file.

---

## 3. Content inventory — every single thing the docs must explain

The complete list of topics the documentation must explain, end-to-end. Each is
mapped to a phase and to the pages that ship it. **[shipped]** = present today;
**[gap]** = planned in the phases.

### 3.1 Why use Void **[shipped]** — `docs/why-void.md`
- Positioning vs Material for MkDocs and the built-in `mkdocs`/`readthedocs`
  themes: distinctive-by-default, fast + app-like, private by default.
- The three pillars (see `WHY_PLAN.md` §1).
- Design language: Glass morphism + NothingOS black canvas + dot-matrix +
  Nothing Red — what it is, where it came from, why it is unique.
- Honest limitations (no-JS, `backdrop-filter` browser support, GitHub rate
  limits on the repo popover).
- **Gap:** none — page ships; keep the comparison table dated and sourced.

### 3.2 How to use (the journey) **[shipped]**
1. **Install** — `pip install mkdocs-void` (`docs/getting-started/installation.md`).
2. **Quick start** — minimal `mkdocs.yml`, `mkdocs serve`, first look
   (`docs/getting-started.md`).
3. **Everyday workflow** — write markdown, run `mkdocs serve --dirtyreload`,
   preview, use page-level front-matter overrides.
4. **Deploy** — GitHub Pages (`docs/deployment.md`), any static host, Docker.

### 3.3 How to configure (the Bible) **[shipped + gap]**
- Every `theme.*` key: `name`, `logo`, `favicon`, `language`, `direction`,
  `palette`, `font` (works — drives the Google Fonts link AND the
  `--void-font-body`/`--void-font-mono` tokens), `features` (Material-compatible
  passthrough).
- Every `theme.void.*` key — the full token groups (colors, typography,
  spacing, border_radius, transitions, shadows), component toggles, header /
  footer / sidebar / toc / search / content / keyboard / reading_mode /
  action_cluster / timer / config_builder / ai_reader / i18n / breadcrumbs /
  pwa / custom_css / custom_js, and the plugin options (`glass`, `dot_matrix`,
  `animation`, `border`, `highlight`, `notes`, `notes_ttl`).
- Every `extra.*` key: `void_version`, `void_logo_dark/light`,
  `void_favicon_dark/light`, `void_og_image`, `void_theme_color`,
  `void_manifest`, `void_twitter_handle`, `void_site_tagline`,
  `void_site_badge`, `void_showcase`, custom head/body/html attrs.
- Plugin block: `plugins: [search, void]` — plus the full passthrough of
  `theme.void.*` on `- void:`.
- Markdown extensions: the recommended set and what each unlocks (admonitions,
  tabs, superfences/mermaid, highlight, tasklist, arithmatex, footnotes,
  snippets, attr_list, def_list …).
- Kitchen-sink "Full configuration" example (README + configuration page).
- **Gap:** component-toggle before/after screenshots; per-section anchor links
  into the generated mega-page (it is currently one include).

### 3.4 Design system **[shipped]**
- Colors: tokens, light/dark palettes, Nothing Red accent, contrast rules
  (`docs/design/colors.md`).
- Typography: Space Grotesk / Space Mono, scale, usage rules, override path
  (`docs/design/typography.md`).
- Glass: light/medium/heavy, blur/saturation/opacity table, offline caveat
  (`docs/design/glass.md`).
- Dot-matrix, borders, animations (incl. `prefers-reduced-motion`), shadows,
  radius, spacing, scrollbar, selection (`docs/design/overview.md`).
- **Gap:** a design-token override workshop showing a real re-brand end-to-end.

### 3.5 Components (each page: what → when → markdown → config → screenshot) **[shipped]**
admonitions, buttons, cards, classes, code-highlighting, diagrams (mermaid),
forms, footnotes, images & SVG (lightbox/lazy/dark-aware), math (KaTeX), notes
(annotations + TTL + export), shortcuts, tables, tabs, task-lists, toast, trees,
engagement (feedback + announcement bar + cookie consent + comments).

### 3.6 Features & behavior **[gap — Phase 5]**
A single `docs/features/index.md` hub (there is no such page today) that lists:
- Search (full-screen modal, `/`, suggestions, context snippets, highlighting,
  share/copy-link per result).
- Reading mode (`Alt+Shift+R`), action cluster (`Alt+Shift+A`), focus timer
  (`Alt+Shift+T`), notes panel (`Ctrl+Shift+N`), keyboard-help modal (`?`),
  repo popover (`Ctrl+Shift+G`), palette toggle (`Ctrl+Shift+L`), sidebar
  (`Ctrl+Shift+B`) and TOC (`Ctrl+Shift+T`) collapse.
- SPA navigation & scroll restore; reading progress; back-to-top; prev/next.
- Service worker caching (`void/templates/sw.js`): static, CDN, versioned
  passthrough (`?v=N`); PWA manifest.
- Persistence: palette, task-list state, notes TTL, collapsed states, reading
  mode, announcement dismissal.
- Graceful-degradation table for every feature: *no-JS*, *offline*, *reduced
  motion*, *no `backdrop-filter`*.

### 3.7 Plugins & integrations **[shipped]**
- First-party: `search`, `void` (`docs/plugins/void.md`).
- Recommended third-party ("full house" build in CI, `docs/plugins/integrations.md`):
  `mkdocs-git-revision-date-localized-plugin`, `mkdocs-glightbox`,
  `mkdocs-section-index`, `mkdocs-print-site`, `mkdocs-table-reader`,
  `mkdocs-awesome-pages`.

### 3.8 Architecture & internals **[shipped]**
- File map, data flow, build pipeline (Sass→PostCSS→cssnano), asset versioning
  (`?v=`), template blocks, init registry in `void.js`, config injection
  (`__config`), theme vs plugin boundaries (`docs/architecture.md`).

### 3.9 Development & contribution **[shipped + gap]**
- Env setup, commands, lint/format, tests, screenshot generation, clean, release
  (`docs/development.md`) and performance/benchmarks (`docs/performance.md`,
  `docs/benchmarks.md`).
- **Gap:** `docs/contributing.md` and `docs/testing.md` do not exist yet
  (Phase 6).

### 3.10 Troubleshooting, FAQ, compatibility **[shipped + gap]**
- Troubleshooting (`docs/troubleshooting.md`), FAQ (`docs/faq.md`).
- **Gap:** a compatibility matrix page (MkDocs 1.5/1.6/2.0.dev; node; browsers)
  and a migration guide from Material/readthedocs (Phase 6).

### 3.11 Learning curve ("Learn" track) **[gap — Phase 6]**
- **Level 1 — Explorer (30 min):** why + install + quick start + tour.
- **Level 2 — Maker (1–2 h):** write docs, styling, components, deploy.
- **Level 3 — Customizer (half day):** design tokens, component toggles,
  header/footer, custom CSS/JS, page-level control.
- **Level 4 — Contributor (ongoing):** architecture, dev loop, tests, recipes.

### 3.12 Community **[shipped]**
- Showcase (`docs/showcase.md`), "Powered by Void" footer credit + badge
  (`void_showcase: true`), Identity & i18n (`docs/identity.md`, incl.
  "Translating Void"), about/credits (`docs/about.md`), funding (GitHub
  Sponsors + Open Collective on PyPI).

---

## 4. Target documentation map (nav of the finished site)

Current `nav` (from `mkdocs.yml`) with planned additions marked **✚** (new) or
**❄** (expand/regenerate):

```yaml
nav:
  - Home: index.md                    ❄  (deep design + feature breakdown)
  - Why Void: why-void.md
  - Showcase: showcase.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Configuration: getting-started/configuration.md   ❄ (generated reference)
    - Quick Start: getting-started.md
  - Design System:
    - Overview: design/overview.md
    - Colors: design/colors.md
    - Typography: design/typography.md
    - Glass Effects: design/glass.md
  - Identity & i18n: identity.md
  - Components: (19 pages, full inventory §3.5)
    - Admonitions / Notes / Diagrams / Code Highlighting / Footnotes / Trees /
      Task Lists / Tabs / Buttons / Cards / Forms / Tables / Math / Images & SVG /
      Toast / CSS Classes / Keyboard Shortcuts / Feedback & Announcements
  - Plugins:
    - Void Plugin: plugins/void.md
    - Third-Party Integrations: plugins/integrations.md
  - Features & Behavior: features/index.md               ✚ (Phase 5)
    - Search / Reading mode / Action cluster / Focus timer / SPA / Offline …  ✚
  - Architecture: architecture.md
  - Performance: performance.md
  - Benchmarks: benchmarks.md
  - Development: development.md
  - Deployment: deployment.md
  - Contributing: contributing.md                        ✚ (Phase 6)
  - Testing & Harnesses: testing.md                      ✚ (Phase 6)
  - Reference:
    - Troubleshooting: troubleshooting.md
    - FAQ: faq.md
    - Compatibility: compatibility.md                    ✚ (Phase 6)
    - Migration: migration.md                            ✚ (Phase 6)
  - Learn: (four-level learning curve)                   ✚ (Phase 6)
    - Explorer / Maker / Customizer / Contributor
  - Screenshots: screenshots.md
  - About: about.md
```

❄ = existing page that gets expanded/regenerated; ✚ = new page.

---

## 5. GitHub Wiki plan

**Goal:** a living, community-editable companion that stays in sync with the
canonical docs without duplicating them.

1. **Create/enable the wiki** for `rkriad585/mkdocs-void` (GitHub → Settings →
   Wiki → Enable). Wiki is a separate git repo:
   `https://github.com/rkriad585/mkdocs-void.wiki.git`.
2. **Seed structure** (mirrors the docs map so navigation is predictable):
   - `Home.md` — entry point, links back to the docs site, "how to use this wiki".
   - `Why-Void.md` — concise pitch (subset of `docs/why-void.md`).
   - `Quick-Start.md` — copy of the quick start (kept deliberately short).
   - `Configuration-Bible.md` — link-out to the generated site reference + top 20
     keys inline for offline/quick glance.
   - `Recipes.md` — community recipes hub (freshness tracking, lightbox, PDF…).
   - `Release-Notes.md` — curated release highlights (links full `CHANGELOG.md`).
   - `Screenshots.md` — gallery embeds.
   - `Contributing-to-the-Wiki.md` — editing guide (clone, branch, PR).
3. **Sidebar** (`_Sidebar.md`): the 8 wiki pages + prominent "full docs →" link.
4. **Sync automation ("wiki never rots")**: a GitHub Action that pushes stable
   seeded pages (`Quick-Start`, `Why-Void`) into the wiki repo on release;
   community edits live one-way *beneath* those seeded pages.
5. **Cross-link contract:** every wiki page that duplicates content links to the
   canonical `https://rkriad585.github.io/mkdocs-void/...` page; every docs page
   that has a wiki counterpart mentions it. **The "docs/READMEs never link
   plan files" rule applies to the wiki too** — wiki pages never link to any
   PLAN file; they link to the live docs site and the `CHANGELOG.md`.

---

## 6. Phases

Each phase: **Goal · Why it matters · What ships · Example · Files · Acceptance.**
Phases are ordered so each one leaves the docs *usable* and *self-consistent*.
Every phase carries the same three checklist lines — the last of them is the
**no-plan-links rule**:

> - **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
>   `tools/check_docs.py` pass.
> - **Documentation rule:** docs and READMEs never link or embed any PLAN file
>   (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 1 — Audit & doc health

**Goal.** Make every doc page honest: no broken links, no dead config talk, no
missing screenshots, searchable titles, generated reference always current.

**Why it matters.** Everything else builds on a trustworthy base. Broken promises
here are why a first-time reader bounces.

**What ships.**
- New `tools/check_docs.py` (does not exist today), run in CI:
  - every `docs/` link resolves; every referenced screenshot exists;
  - every config key used in the docs exists in the plugin/templates;
  - one H1 per page; no `TODO`/`FIXME`;
  - no `docs/**` page or README contains a link to any PLAN file (Rule 11).
- `doc files ↔ nav` reconciliation: every page in `docs/` either appears in
  `mkdocs.yml` `nav` or lands in `not_in_nav` (today `_config_ref.generated.md`).
- Screenshot contract: `docs/screenshots.md` ↔ `Screenshots/*.png` reconciliation.

```python
# tools/check_docs.py (new, run in CI)
import pathlib, re, sys
ROOT = pathlib.Path(__file__).parent.parent
docs = ROOT / "docs"
plans = ("PLAN.md", "WHY_PLAN.md", "RENAME-PLAN.md", "DOCS_WIKI_PLAN.md")
md_links = re.compile(r"\]\(([^)]+\.md[^)]*)\)")
plan_hits = re.compile(r"\]\((?:\.\./)*(" + "|".join(plans) + r")[^)]*\)", re.I)
missing, banned = [], []
for page in docs.rglob("*.md"):
    text = page.read_text(encoding="utf-8")
    banned += [f"{page}: links a PLAN file" for _ in plan_hits.findall(text)]
    for target in md_links.findall(text):
        t = target.split("#")[0].split("?")[0]
        if t and t.endswith(".md") and not (docs / t).exists():
            missing.append(f"{page} -> {t}")
if missing or banned:
    print("\n".join(missing + banned)); sys.exit(1)
print(f"doc link + plan-link check OK across {len(list(docs.rglob('*.md')))} pages")
```

**Files.** `docs/**`, `tools/check_docs.py` (new), `.github/workflows/*`,
`mkdocs.yml` (nav corrections only).

**Acceptance.** All intra-doc links resolve; screenshot contract clean; no doc
talks about a config key the theme ignores; no PLAN-file links anywhere;
`tools/check_docs.py` passes → wired into CI.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 2 — Why & onboarding

**Goal.** Within 5 minutes a reader understands *what Void is, why it exists,
and how to go live*.

**Why it matters.** First impressions decide whether the docs get read at all.

**What ships.**
- `docs/why-void.md` **❄** — refresh the comparison table (dated + sourced),
  link the three pillars, keep the honest-limitations section. **[shipped base]**
- `docs/showcase.md` — keep real sites + the Screenshots gallery working.
- `docs/getting-started.md` **❄** — minimal config → `mkdocs serve` → tour of
  each page region (header, sidebar, TOC, footer, cluster, notes, timer).
- `docs/getting-started/model-project.md` **✚** — new annotated full project
  layout (folder tree, where assets live, how the plugin merges `theme.void`
  and `- void:`).

**Example — quickest possible start:**

```yaml
# mkdocs.yml — the entire config a new site needs
site_name: My Docs
theme:
  name: void
```

```bash
pip install mkdocs-void
mkdocs new my-docs && cd my-docs
# paste the two-line config above
mkdocs serve
```

**Files.** `docs/why-void.md`, `docs/showcase.md`, `docs/getting-started.md`,
`docs/getting-started/model-project.md` (new).

**Acceptance.** Following the quick start from clean machine → visible site in
under 5 minutes; showcase links resolve; every "region" of the tour matches the
rendered page.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 3 — Configuration Bible

**Goal.** Every configuration key a developer could ever set is documented with
default, purpose, example, and effect — generated, not hand-typed.

**Why it matters.** The config surface is the theme's biggest download; the
reference is what makes it usable.

**What ships.**
- `tools/emit_config_reference.py` → `docs/_config_ref.generated.md` →
  snippets-included into `docs/getting-started/configuration.md`. **[shipped]**
- Per-section anchor links into the generated mega-page (nav + "jump to" table
  at the top), kept under one mega-page until it passes ~600 rendered lines.
- Component-toggle before/after screenshots: each `components.*.show` switch
  documented with a rendered-with/rendered-without pair.
- Kitchen-sink config example: every option set, commented, copyable and
  bisectable.

**Example — the generated table contract:**

```markdown
<!-- auto-generated, do not edit: tools/emit_config_reference.py -->
### `theme.void.colors.primary`

| | |
|---|---|
| Default | `"#ff3030"` |
| CSS variable | `--void-accent` |
| Purpose | Accent color for active states, links, progress |
| Example | `primary: "#00ff88"` |

> Drives `--void-accent`. Regenerate with `python tools/emit_config_reference.py`.
```

**Files.** `tools/emit_config_reference.py`, `docs/getting-started/configuration.md`,
`docs/getting-started/_config_ref.generated.md`, `mkdocs.yml` nav.

**Acceptance.** Every key in the plugin/templates appears in the reference with a
default; the kitchen-sink config builds clean; reference regenerates
deterministically (CI diff check); each documented toggle has a before/after
screenshot.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 4 — Design system & components deep-dive

**Goal.** Every design token and every component has a page that shows what it
is, when to use it, how to write it in Markdown, and how it looks — and the
home page demonstrates the design language in depth.

**Why it matters.** This is the "wow" layer that separates Void from othered
themes; it must be demonstrative, not descriptive.

**What ships.**
- Expand `docs/design/*`: color token table + contrast; the glass table
  (light/medium/heavy: blur, saturation, opacity, browser support); dot-matrix
  config; borders; animations + `prefers-reduced-motion`; shadows; spacing;
  radius; scrollbar; selection. **[shipped base]**
- **❄** `docs/index.md` — in-depth **Design Principles** and **Features**
  breakdown, written with the theme's own components (admonitions, tabs, task
  lists, footnotes, a mermaid diagram, KaTeX math, image lightbox, code
  highlighting) so the home page doubles as a living showcase. [Phase 4 cliff
  item — shipped in the index rewrite batch]
- Lock every `docs/components/*` page to the fixed 7-section template:

```markdown
# {Component}

## What it is
{1–2 sentences}

## When to use it
{when this element earns its keep, when to avoid it}

## In Markdown
```markdown{...copied so it works out of the box...}
## Configuration
| Key | Default | Effect |
## Live preview / screenshot
![{component}](...)
## Under the hood
{file, class names, data-attributes}
## Accessibility notes
```
- Design-token re-brand workshop **✚** (`docs/design/rebranding.md`): one page
  showing a full brand swap from tokens to header/footer/sidebar — the docs
  side of "customizer" learning.

**Files.** `docs/design/*`, `docs/components/*`, `docs/index.md`,
`tools/screenshots_gen.py`, `Screenshots/*`.

**Acceptance.** Every §3.5 component exists with the 7-section template filled;
component screenshots exist and are referenced; design table contents match SCSS
source (spot-checked in CI); the home page demonstrates every component family.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 5 — Features & behavior index

**Goal.** Document the interactive behavior that makes Void feel like an app,
including what happens offline and without JS.

**Why it matters.** Half the theme's value is invisible in static screenshots;
readers must learn the shortcuts and behaviors somewhere coherent.

**What ships.**
- `docs/features/index.md` **✚** + sub-pages: search, reading mode, action
  cluster, focus timer, notes panel, keyboard reference, SPA navigation & scroll
  restore, service worker & caching (diagram of `sw.js` strategy), PWA manifest,
  repo popover (fields, caching, rate limits), persistence (palette, task lists,
  notes TTL, collapsed states, announcement dismissal), reading progress, TOC
  scrollspy, back-to-top.
- Graceful-degradation table: for each feature — *no-JS*, *offline*, *reduced
  motion*, *no `backdrop-filter`* — what the user still gets.

**Example — service worker page skeleton:**

```markdown
# Service worker & offline

- **File:** `void/templates/sw.js`
- **Caches:** `void-static-v3` (same-origin assets, stale-while-revalidate),
  `void-cdn-v3` (fonts/CDN, cache-first).
- **Versioned URLs** (`?v=N`) pass through to the browser HTTP cache — that is
  how new releases bypass stale SW copies (see asset versioning).
- **Offline behavior:** a cached page still opens; search index is *not* cached
  by the SW by design (MkDocs worker owns it).

| Scenario | What works |
|---|---|
| Online | everything |
| Offline, previously visited | page renders from cache; CDN assets hit `void-cdn-v3` |
| Offline, never visited | fallback? currently no — document honestly |
```

**Files.** `docs/features/**` (new), `mkdocs.yml` nav.

**Acceptance.** Every behavior has a page; behavior matches the code (verified
by the existing harnesses referenced from the docs); degradation table filled.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 6 — Developer docs & learning curve

**Goal.** Someone can go from reader to contributor with a guided path, and every
"learning level" has a concrete tutorial.

**Why it matters.** Retention and contributions come from a clear path, not
hidden knowledge.

**What ships.**
- `docs/architecture.md` **❄** (`[shipped] base`, expand where needed) + a new
  `docs/contributing.md` **✚**: issue labels, first-issue path, PR checklist,
  testing expectations, docs-PR etiquette (screenshots required).
- NEW `docs/testing.md` **✚**: what each test covers + how to add one (the
  void.test.js checks, harnesses, recipes).
- NEW `docs/reference/compatibility.md` **✚**: MkDocs 1.5/1.6/2.0.dev, node
  versions, browser support matrix.
- NEW `docs/reference/migration.md` **✚**: from `mkdocs`/`readthedocs`/Material.
- NEW `docs/learn/*` **✚** — the four-level learning curve (§3.11), each level
  ending in a "verify you got it" checklist tied to the model project.

**Example — Level checkpoints:**

```markdown
### Level 2 — Maker ✅ you have:
- [ ] a live site at `mkdocs serve`
- [ ] a component page using admonitions, tabs, and task lists
- [ ] changed one design token and seen it apply
- [ ] deployed to GitHub Pages once
```

**Files.** `docs/architecture.md`, `docs/development.md`, `docs/contributing.md`,
`docs/testing.md`, `docs/reference/compatibility.md`, `docs/reference/migration.md`,
`docs/learn/**`, `CONTRIBUTING.md` (cross-link only).

**Acceptance.** A first-time contributor completes the Contributor level with
only these docs open; every command cited runs on a fresh clone.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 7 — GitHub Wiki

**Goal.** Legacy-visible, community-editable companion that stays truthful.

**Why it matters.** Some readers live on GitHub; the wiki is their safety net and
gives the community a place to contribute without touching the repo.

**What ships.**
- Enable + seed the wiki per §5; `_Sidebar.md`, `Home.md`, `Why-Void.md`,
  `Quick-Start.md`, `Configuration-Bible.md`, `Recipes.md`, `Release-Notes.md`,
  `Screenshots.md`, `Contributing-to-the-Wiki.md`.
- GitHub Action (`tools/wiki_sync/`) pushing the seed pages on release.
- `docs/contributing.md` section "Contributing to the Wiki".

**Example — wiki Home.md:**

```markdown
# mkdocs-void wiki

Everything quick about Void. Full canonical docs live at
**[https://rkriad585.github.io/mkdocs-void/](https://rkriad585.github.io/mkdocs-void/)**.

- [Why Void](Why-Void)
- [Quick Start](Quick-Start)
- [Configuration Bible](Configuration-Bible)
- [Recipes](Recipes)
- [Release Notes](Release-Notes)
- [Screenshots](Screenshots)
- [Contribute to this wiki](Contributing-to-the-Wiki)
```

**Files.** wiki repo, `.github/workflows/wiki-sync.yml`, `tools/wiki_sync/`,
`docs/contributing.md`.

**Acceptance.** Wiki accessible at `github.com/rkriad585/mkdocs-void/wiki`;
every page links back to canonical docs; sync Action runs green on tag; no wiki
page links to any PLAN file.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 8 — AI-readable, PWA & i18n

**Goal.** Finish documenting the modern surfaces the theme already ships and
make the docs site a first-class citizen of the AI/offline world.

**Why it matters.** These features ship but have no dedicated docs page; readers
end up grepping `mkdocs.yml` to find them.

**What ships.**
- `docs/features/ai-readable.md` **✚**: AI-readable mode — per-page markdown
  mirrors, watermarks, `llms.txt`, `llms-full.txt`, sitemap mirror URLs; how to
  enable/disable, `url_style`, `exclude`, `description`.
- `docs/features/pwa.md` **✚**: manifest fields, icons, theme_color, start_url,
  display modes, `assets.mode` (cdn/local/bundle), SW caching, how to test.
- `docs/translating.md` **✚**: i18n flat aliases, brand strings, search/TOC
  labels, the string inventory, how a future locale registers (see also
  "Translating Void" in `docs/identity.md`).

**Files.** `docs/features/*` (new), `docs/translating.md` (new), `mkdocs.yml` nav.

**Acceptance.** Each feature page reproduces its real defaults;
`llms.txt`/`manifest.webmanifest` behavior in the docs build matches the page;
a translated string example renders.

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

### Phase 9 — Quality, CI & maintenance

**Goal.** The docs stay correct forever with zero manual effort.

**Why it matters.** Without gates, every earlier phase rots.

**What ships.**
- CI jobs: `tools/check_docs.py` (links/screenshots/H1/plan-link ban),
  config-reference diff, docs-examples build (each snippet), screenshot
  regeneration on demand, benchmarks/Lighthouse already live
  (`.github/workflows/performance.yml` runs LHCI 3× and asserts the median).
- Search-index freshness: search plugin runs in the docs build (already active);
  newly added pages indexed automatically.
- Release notes ↔ `CHANGELOG.md` alignment: every tagged release updates `docs/`
  release notes and wiki `Release-Notes.md` (existing Release workflow already
  emits the changelog commit + publishes PyPI).
- i18n/translation readiness (`docs/translating.md` from Phase 8).
- RSS/sitemap/`llms.txt` wiring checks.

**Files.** `.github/workflows/*`, `tools/check_docs.py`, `docs/translating.md`,
`docs/**` release fragments.

**Acceptance.** `git push` → CI green proves docs health; a release
automatically syncs wiki + changelog + PyPI; search covers new pages without
manual steps; no PLAN-file links ever reappear (fails CI).

- **Verification:** `npm run build`, `mkdocs build --strict`, `npm test`,
  `tools/check_docs.py` pass.
- **Documentation rule:** docs and READMEs never link or embed any PLAN file
  (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`, `DOCS_WIKI_PLAN.md`).

---

## 7. Definition of done

`DOCS_WIKI_PLAN.md` is complete when:

1. **Nothing in §3 is undocumented** — every inventory item maps to a page.
2. **Generated reference is canonical** — no hand-maintained config duplication.
3. **Every example is tested** in CI; no snippet rots.
4. **Screenshots exist for every visual claim** and are regenerable.
5. **Learning curve is real** — four levels with checkpoints, each completable
   using only the docs.
6. **Wiki is alive** — seeded, linked, auto-synced, and invites contribution.
7. **CI owns the quality** — link checks, reference diff, example builds,
   screenshot checks, and the plan-link ban all fail the build on drift.
8. **Docs & READMEs stand alone** — no `docs/**` page or README links or embeds
   any PLAN file (`PLAN.md`, `WHY_PLAN.md`, `RENAME-PLAN.md`,
   `DOCS_WIKI_PLAN.md`).
9. **Mandatory Working Rules respected** in every phase — no deletions, no
   typos, no out-of-scope edits, nothing half-shipped.

---

## 8. Risks & constraints

| Risk | Mitigation |
|---|---|
| Docs drift from code | Generated reference + CI diff; expand only via `tools/emit_config_reference.py` |
| Wiki goes stale | Release-sync Action; seed pages are the only duplicated content and are one-way pushed |
| Screenshots rot | Regenerate via `screenshots_gen.py`; `check_docs.py` fails on missing files |
| Snippets rot | Recipe/integration project builds every snippet in CI |
| Maintenance-mode Material comparisons age | Date + source every comparison; keep table small and updatable |
| MkDocs 2.0 changes page/plugin APIs | Compatibility page + CI matrix (1.5/1.6/2.0.dev) dedicated to docs accuracy |
| Plan files leak into docs/READMEs | Rule 11 enforced per phase + `check_docs.py` CI ban |

---

## 9. Supporting plans & artifacts

Working contracts that feed the phases above (this is where the "more plan",
as asked, lives):

### 9.1 Page template contract
Every doc page (except the index and generated reference) uses:
`title` front matter → one `# H1` → sections with `##`/`###` only, unique H1 per
page, `date:` front matter when relevant, links relative within `docs/`, and a
"See also" row when a related page exists. No page contains `TODO`/`FIXME`.

### 9.2 Screenshot contract
`tools/screenshots_gen.py` owns the gallery. Naming = the page they illustrate
(`home.png`, `buttons.png`, …). The docs build fails if `docs/screenshots.md`
references a missing file. Any component page that shows HTML must have a
matching screenshot.

### 9.3 Generated-reference contract
`tools/emit_config_reference.py` emits from `_VOID_TOKEN_MAP` + `_void_defaults`
only. The output header says "generated: do not edit". CI diffs the output;
regressions fail the build. Humans never hand-edit `_config_ref.generated.md`.

### 9.4 Wiki sync design
Release-triggered workflow clones
`git@github.com:rkriad585/mkdocs-void.wiki.git`, overwrites the seed pages,
commits with `[skip ci]`, pushes. Community-only pages are never touched.
Conflicts are impossible because the workflow force-updates only its own
listed files.

### 9.5 AI-agent contract
Every page must be readable by an agent: canonical URL, description (or title),
watermarked mirror, `llms.txt` entry. Document `llms.txt` + mirror URL scheme in
the AI-readable page (Phase 8) so agents and humans share one contract.

### 9.6 Release documentation checklist
For every `v*` tag: bump version (pyproject, `void/__init__.py`, `package.json`,
docs tree), CHANGELOG prose under `[Unreleased]`, Release workflow publishes
PyPI (skip-existing), auto-pushes the changelog commit, and wiki seed pages sync.
Verify `https://pypi.org/pypi/mkdocs-void/json` (project URLs sane — no dead
Tidelift/Patreon-style links).

### 9.7 Benchmarks & Lighthouse
`.github/workflows/performance.yml` runs 3 Lighthouse runs on a shared runner
and asserts the **median** (per-run mobile scores can compute null on shared
runners). `docs/benchmarks.md` is CI-regenerated. Never lower thresholds to pass
a flaky run — investigate first.

### 9.8 i18n strategy
i18n keys are flat aliases over the nested client strings (`search_`,
`toc_`, `back_to_top`, `copy_to_clipboard`, …). A locale = a YAML map merged
over defaults. `docs/translating.md` (Phase 8) defines how a translator ships a
locale and how it is tested (spot-render in CI).

### 9.9 Config-builder docs approach
`config_builder` is a **dev tool, OFF by default**. The docs site turns it on to
showcase it (gear in the cluster + pinned TOC trigger). Its docs live in the
Configuration page and the components section — never in the nav as a product
feature.

### 9.10 Metrics of success
- Quick-start-to-live under 5 minutes (from docs only).
- 100% of §3 inventory documented.
- Zero PLAN-file links in docs/READMEs (CI-enforced).
- Every component page has a screenshot + 7-section template.
- Wiki seeded and auto-synced on the next release.
- AI-readable contract documented (`llms.txt` + mirrors).
- Learning-curve pages: 4 levels, all commands runnable on a fresh clone.

---

*DOCS_WIKI_PLAN.md — documentation + wiki roadmap for mkdocs-void. Update §3
(inventory) and §4 (map) the day a page ships; keep the plan honest like the
docs it plans — and keep planning artifacts out of the docs it plans.*