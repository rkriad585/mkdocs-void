---
date: 2026-09-18
title: Kitchen Sink
icon: "⚗️"
---

# Kitchen Sink

Every `theme.void.*` option at once, each set to its shipped default. Copy
the block into your `mkdocs.yml` under `theme:` and delete what you do not
use — every value here is also valid alone, because it equals the default the
plugin would merge anyway.

The block is generated from the same source tables as the
[reference index](configuration.md#options-reference-index) by
`tools/emit_config_reference.py`, so it always matches the current code.

--8<-- "getting-started/configuration/_kitchen_sink.generated.yml"

!!! tip
    The [per-key reference pages](configuration/tokens.md) explain what each
    key does. Design-token values such as `colors.primary` map onto CSS
    custom properties you can also override via `extra_css`.