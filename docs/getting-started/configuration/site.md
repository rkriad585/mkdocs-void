---
title: Configuration - site, integrations & PWA
---

# Configuration - site, integrations & PWA

Generated from the live plugin tables (`_VOID_TOKEN_MAP`, `_void_defaults`, the `_VOID_DEFAULT_*` dicts and the compiled token defaults in `void.scss`) by `tools/emit_config_reference.py`. The page is regenerated in CI and can never drift from the shipped code.

<!-- generated: do not edit. Run `python tools/emit_config_reference.py`. -->

## social_cards

- [social_cards.cards](#themevoidsocial_cardscards) &middot; [social_cards.enabled](#themevoidsocial_cardsenabled) &middot; [social_cards.jsonld](#themevoidsocial_cardsjsonld)

### `theme.void.social_cards.cards`
| | |
|---|---|
| Default | `true` |

### `theme.void.social_cards.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for JSON-LD + auto OG cards. |
| Example | `social_cards: {enabled: true}` |

### `theme.void.social_cards.jsonld`
| | |
|---|---|
| Default | `true` |

## meta

- [meta.branch](#themevoidmetabranch) &middot; [meta.date_source](#themevoidmetadate_source) &middot; [meta.edit_label](#themevoidmetaedit_label) &middot; [meta.enabled](#themevoidmetaenabled) &middot; [meta.last_updated_label](#themevoidmetalast_updated_label) &middot; [meta.show_edit_on_github](#themevoidmetashow_edit_on_github) &middot; [meta.show_last_updated](#themevoidmetashow_last_updated) &middot; [meta.source_dir](#themevoidmetasource_dir)

### `theme.void.meta.branch`
| | |
|---|---|
| Default | `"main"` |

### `theme.void.meta.date_source`
| | |
|---|---|
| Default | `"auto"` |
| Purpose | Where the 'Last updated' date comes from. |
| Example | `meta: {date_source: "auto"}` |

### `theme.void.meta.edit_label`
| | |
|---|---|
| Default | `"Edit this page"` |

### `theme.void.meta.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the last-updated + edit-on-GitHub bar. |
| Example | `meta: {enabled: true}` |

### `theme.void.meta.last_updated_label`
| | |
|---|---|
| Default | `"Last updated"` |

### `theme.void.meta.show_edit_on_github`
| | |
|---|---|
| Default | `true` |

### `theme.void.meta.show_last_updated`
| | |
|---|---|
| Default | `true` |

### `theme.void.meta.source_dir`
| | |
|---|---|
| Default | `"docs"` |

## feedback

- [feedback.enabled](#themevoidfeedbackenabled) &middot; [feedback.github_labels](#themevoidfeedbackgithub_labels) &middot; [feedback.negative](#themevoidfeedbacknegative) &middot; [feedback.positive](#themevoidfeedbackpositive) &middot; [feedback.show](#themevoidfeedbackshow) &middot; [feedback.title](#themevoidfeedbacktitle)

### `theme.void.feedback.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the 'Was this page helpful?' widget (opens an issue). |
| Example | `feedback: {enabled: true}` |

### `theme.void.feedback.github_labels`
| | |
|---|---|
| Default | `[feedback]` |

### `theme.void.feedback.negative`
| | |
|---|---|
| Default | `"No \u2014 open an issue"` |

### `theme.void.feedback.positive`
| | |
|---|---|
| Default | `"Yes \u2014 thanks!"` |

### `theme.void.feedback.show`
| | |
|---|---|
| Default | `true` |

### `theme.void.feedback.title`
| | |
|---|---|
| Default | `"Was this page helpful?"` |

## announcement_bar

- [announcement_bar.dismissable](#themevoidannouncement_bardismissable) &middot; [announcement_bar.enabled](#themevoidannouncement_barenabled) &middot; [announcement_bar.position](#themevoidannouncement_barposition) &middot; [announcement_bar.show](#themevoidannouncement_barshow) &middot; [announcement_bar.text](#themevoidannouncement_bartext)

### `theme.void.announcement_bar.dismissable`
| | |
|---|---|
| Default | `true` |

### `theme.void.announcement_bar.enabled`
| | |
|---|---|
| Default | `false` |
| Purpose | Opt-in announcement card. Renders only when enabled and text is set. |
| Example | `announcement_bar: {enabled: true, text: New in v0.2, position: top}` |

### `theme.void.announcement_bar.position`
| | |
|---|---|
| Default | `"bottom"` |
| Purpose | Floating placement of the announcement card. |
| Example | `announcement_bar: {position: "top"}   # top | right | bottom | left | center` |

### `theme.void.announcement_bar.show`
| | |
|---|---|
| Default | `true` |

### `theme.void.announcement_bar.text`
| | |
|---|---|
| Default | `""` |

## cookie_consent

- [cookie_consent.accept_label](#themevoidcookie_consentaccept_label) &middot; [cookie_consent.decline_label](#themevoidcookie_consentdecline_label) &middot; [cookie_consent.enabled](#themevoidcookie_consentenabled) &middot; [cookie_consent.message](#themevoidcookie_consentmessage) &middot; [cookie_consent.position](#themevoidcookie_consentposition) &middot; [cookie_consent.privacy_policy](#themevoidcookie_consentprivacy_policy) &middot; [cookie_consent.render](#themevoidcookie_consentrender) &middot; [cookie_consent.show](#themevoidcookie_consentshow)

### `theme.void.cookie_consent.accept_label`
| | |
|---|---|
| Default | `"Accept"` |

### `theme.void.cookie_consent.decline_label`
| | |
|---|---|
| Default | `"Decline"` |

### `theme.void.cookie_consent.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.cookie_consent.message`
| | |
|---|---|
| Default | `"This site stores nothing about you unless you enable integrations."` |

### `theme.void.cookie_consent.position`
| | |
|---|---|
| Default | `"bottom"` |

### `theme.void.cookie_consent.privacy_policy`
| | |
|---|---|
| Default | `""` |

### `theme.void.cookie_consent.render`
| | |
|---|---|
| Default | `"auto"` |
| Purpose | When the consent banner renders: only with an integration, always, or never. |
| Example | `cookie_consent: {render: "auto"}   # "auto" | "always" | "never"` |

### `theme.void.cookie_consent.show`
| | |
|---|---|
| Default | `true` |

## comments

- [comments.category](#themevoidcommentscategory) &middot; [comments.category_id](#themevoidcommentscategory_id) &middot; [comments.enabled](#themevoidcommentsenabled) &middot; [comments.language](#themevoidcommentslanguage) &middot; [comments.mapping](#themevoidcommentsmapping) &middot; [comments.provider](#themevoidcommentsprovider) &middot; [comments.repo](#themevoidcommentsrepo) &middot; [comments.repo_id](#themevoidcommentsrepo_id) &middot; [comments.term](#themevoidcommentsterm) &middot; [comments.theme.dark](#themevoidcommentsthemedark) &middot; [comments.theme.light](#themevoidcommentsthemelight)

### `theme.void.comments.category`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.category_id`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.enabled`
| | |
|---|---|
| Default | `false` |
| Purpose | Opt-in giscus comments. Requires repo + repo_id to actually render. |
| Example | `comments: {enabled: true}` |

### `theme.void.comments.language`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.mapping`
| | |
|---|---|
| Default | `"pathname"` |
| Purpose | How a page maps to a giscus discussion. |
| Example | `comments: {mapping: "pathname"}` |

### `theme.void.comments.provider`
| | |
|---|---|
| Default | `"giscus"` |

### `theme.void.comments.repo`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.repo_id`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.term`
| | |
|---|---|
| Default | `""` |

### `theme.void.comments.theme.dark`
| | |
|---|---|
| Default | `"dark"` |

### `theme.void.comments.theme.light`
| | |
|---|---|
| Default | `"light"` |

## breadcrumbs

- [breadcrumbs.show](#themevoidbreadcrumbsshow)

### `theme.void.breadcrumbs.show`
| | |
|---|---|
| Default | `true` |
| Purpose | Toggles the breadcrumb trail above the article. |
| Example | `breadcrumbs: {show: true}` |

## pwa

- [pwa.background_color](#themevoidpwabackground_color) &middot; [pwa.display](#themevoidpwadisplay) &middot; [pwa.icons](#themevoidpwaicons) &middot; [pwa.manifest](#themevoidpwamanifest) &middot; [pwa.start_url](#themevoidpwastart_url) &middot; [pwa.theme_color](#themevoidpwatheme_color)

### `theme.void.pwa.background_color`
| | |
|---|---|
| Default | `"#111114"` |

### `theme.void.pwa.display`
| | |
|---|---|
| Default | `"standalone"` |
| Purpose | PWA display mode. |
| Example | `pwa: {display: "standalone"}` |

### `theme.void.pwa.icons`
| | |
|---|---|
| Default | `true` |

### `theme.void.pwa.manifest`
| | |
|---|---|
| Default | `true` |
| Purpose | Auto-generates manifest.webmanifest so the site is installable. |
| Example | `pwa: {manifest: true}` |

### `theme.void.pwa.start_url`
| | |
|---|---|
| Default | `""` |

### `theme.void.pwa.theme_color`
| | |
|---|---|
| Default | `""` |

## assets

- [assets.inline_critical_css](#themevoidassetsinline_critical_css) &middot; [assets.mode](#themevoidassetsmode) &middot; [assets.timeout](#themevoidassetstimeout) &middot; [assets.vendor_dir](#themevoidassetsvendor_dir)

### `theme.void.assets.inline_critical_css`
| | |
|---|---|
| Default | `false` |
| Purpose | Inline the critical subset of the theme CSS into the HTML head. |
| Example | `assets: {inline_critical_css: false}` |

### `theme.void.assets.mode`
| | |
|---|---|
| Default | `"cdn"` |
| Purpose | Library loading mode: cdn (default), self-hosted local, or concatenated bundle. |
| Example | `assets: {mode: "cdn"}   # "cdn" | "local" | "bundle"` |

### `theme.void.assets.timeout`
| | |
|---|---|
| Default | `20` |

### `theme.void.assets.vendor_dir`
| | |
|---|---|
| Default | `"assets/vendor"` |

