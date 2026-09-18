---
title: Configuration - shortcuts & interaction
---

# Configuration - shortcuts & interaction

Generated from the live plugin tables (`_VOID_TOKEN_MAP`, `_void_defaults`, the `_VOID_DEFAULT_*` dicts and the compiled token defaults in `void.scss`) by `tools/emit_config_reference.py`. The page is regenerated in CI and can never drift from the shipped code.

<!-- generated: do not edit. Run `python tools/emit_config_reference.py`. -->

## keyboard

- [keyboard.custom](#themevoidkeyboardcustom) &middot; [keyboard.enabled](#themevoidkeyboardenabled) &middot; [keyboard.shortcuts.close.enabled](#themevoidkeyboardshortcutscloseenabled) &middot; [keyboard.shortcuts.close.key](#themevoidkeyboardshortcutsclosekey) &middot; [keyboard.shortcuts.close.label](#themevoidkeyboardshortcutscloselabel) &middot; [keyboard.shortcuts.help.enabled](#themevoidkeyboardshortcutshelpenabled) &middot; [keyboard.shortcuts.help.key](#themevoidkeyboardshortcutshelpkey) &middot; [keyboard.shortcuts.help.label](#themevoidkeyboardshortcutshelplabel) &middot; [keyboard.shortcuts.search.enabled](#themevoidkeyboardshortcutssearchenabled) &middot; [keyboard.shortcuts.search.key](#themevoidkeyboardshortcutssearchkey) &middot; [keyboard.shortcuts.search.label](#themevoidkeyboardshortcutssearchlabel) &middot; [keyboard.shortcuts.search_down.enabled](#themevoidkeyboardshortcutssearch_downenabled) &middot; [keyboard.shortcuts.search_down.key](#themevoidkeyboardshortcutssearch_downkey) &middot; [keyboard.shortcuts.search_down.label](#themevoidkeyboardshortcutssearch_downlabel) &middot; [keyboard.shortcuts.search_open.enabled](#themevoidkeyboardshortcutssearch_openenabled) &middot; [keyboard.shortcuts.search_open.key](#themevoidkeyboardshortcutssearch_openkey) &middot; [keyboard.shortcuts.search_open.label](#themevoidkeyboardshortcutssearch_openlabel) &middot; [keyboard.shortcuts.search_up.enabled](#themevoidkeyboardshortcutssearch_upenabled) &middot; [keyboard.shortcuts.search_up.key](#themevoidkeyboardshortcutssearch_upkey) &middot; [keyboard.shortcuts.search_up.label](#themevoidkeyboardshortcutssearch_uplabel) &middot; [keyboard.shortcuts.tab_left.enabled](#themevoidkeyboardshortcutstab_leftenabled) &middot; [keyboard.shortcuts.tab_left.key](#themevoidkeyboardshortcutstab_leftkey) &middot; [keyboard.shortcuts.tab_left.label](#themevoidkeyboardshortcutstab_leftlabel) &middot; [keyboard.shortcuts.tab_right.enabled](#themevoidkeyboardshortcutstab_rightenabled) &middot; [keyboard.shortcuts.tab_right.key](#themevoidkeyboardshortcutstab_rightkey) &middot; [keyboard.shortcuts.tab_right.label](#themevoidkeyboardshortcutstab_rightlabel) &middot; [keyboard.shortcuts.toggle_notes.enabled](#themevoidkeyboardshortcutstoggle_notesenabled) &middot; [keyboard.shortcuts.toggle_notes.key](#themevoidkeyboardshortcutstoggle_noteskey) &middot; [keyboard.shortcuts.toggle_notes.label](#themevoidkeyboardshortcutstoggle_noteslabel) &middot; [keyboard.shortcuts.toggle_reading_mode.enabled](#themevoidkeyboardshortcutstoggle_reading_modeenabled) &middot; [keyboard.shortcuts.toggle_reading_mode.key](#themevoidkeyboardshortcutstoggle_reading_modekey) &middot; [keyboard.shortcuts.toggle_reading_mode.label](#themevoidkeyboardshortcutstoggle_reading_modelabel) &middot; [keyboard.shortcuts.toggle_reading_mode.persisted](#themevoidkeyboardshortcutstoggle_reading_modepersisted) &middot; [keyboard.shortcuts.toggle_repo_popover.enabled](#themevoidkeyboardshortcutstoggle_repo_popoverenabled) &middot; [keyboard.shortcuts.toggle_repo_popover.key](#themevoidkeyboardshortcutstoggle_repo_popoverkey) &middot; [keyboard.shortcuts.toggle_repo_popover.label](#themevoidkeyboardshortcutstoggle_repo_popoverlabel) &middot; [keyboard.shortcuts.toggle_scheme.enabled](#themevoidkeyboardshortcutstoggle_schemeenabled) &middot; [keyboard.shortcuts.toggle_scheme.key](#themevoidkeyboardshortcutstoggle_schemekey) &middot; [keyboard.shortcuts.toggle_scheme.label](#themevoidkeyboardshortcutstoggle_schemelabel) &middot; [keyboard.shortcuts.toggle_sidebar.enabled](#themevoidkeyboardshortcutstoggle_sidebarenabled) &middot; [keyboard.shortcuts.toggle_sidebar.key](#themevoidkeyboardshortcutstoggle_sidebarkey) &middot; [keyboard.shortcuts.toggle_sidebar.label](#themevoidkeyboardshortcutstoggle_sidebarlabel) &middot; [keyboard.shortcuts.toggle_sidebar.persisted](#themevoidkeyboardshortcutstoggle_sidebarpersisted) &middot; [keyboard.shortcuts.toggle_toc.enabled](#themevoidkeyboardshortcutstoggle_tocenabled) &middot; [keyboard.shortcuts.toggle_toc.key](#themevoidkeyboardshortcutstoggle_tockey) &middot; [keyboard.shortcuts.toggle_toc.label](#themevoidkeyboardshortcutstoggle_toclabel) &middot; [keyboard.shortcuts.toggle_toc.persisted](#themevoidkeyboardshortcutstoggle_tocpersisted)

### `theme.void.keyboard.custom`
| | |
|---|---|
| Default | `[]` |

### `theme.void.keyboard.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the keyboard shortcut system. |
| Example | `keyboard: {enabled: true}` |

### `theme.void.keyboard.shortcuts.close.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.close.key`
| | |
|---|---|
| Default | `"Escape"` |

### `theme.void.keyboard.shortcuts.close.label`
| | |
|---|---|
| Default | `"Close active overlay"` |

### `theme.void.keyboard.shortcuts.help.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.help.key`
| | |
|---|---|
| Default | `"?"` |

### `theme.void.keyboard.shortcuts.help.label`
| | |
|---|---|
| Default | `"Show keyboard shortcuts"` |

### `theme.void.keyboard.shortcuts.search.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.search.key`
| | |
|---|---|
| Default | `"/"` |
| Purpose | Key that opens full-screen search. |
| Example | `keyboard: {shortcuts: {search: {key: /}}}` |

### `theme.void.keyboard.shortcuts.search.label`
| | |
|---|---|
| Default | `"Open search"` |

### `theme.void.keyboard.shortcuts.search_down.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.search_down.key`
| | |
|---|---|
| Default | `"ArrowDown"` |

### `theme.void.keyboard.shortcuts.search_down.label`
| | |
|---|---|
| Default | `"Navigate search results down"` |

### `theme.void.keyboard.shortcuts.search_open.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.search_open.key`
| | |
|---|---|
| Default | `"Enter"` |

### `theme.void.keyboard.shortcuts.search_open.label`
| | |
|---|---|
| Default | `"Open selected result"` |

### `theme.void.keyboard.shortcuts.search_up.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.search_up.key`
| | |
|---|---|
| Default | `"ArrowUp"` |

### `theme.void.keyboard.shortcuts.search_up.label`
| | |
|---|---|
| Default | `"Navigate search results up"` |

### `theme.void.keyboard.shortcuts.tab_left.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.tab_left.key`
| | |
|---|---|
| Default | `"ArrowLeft"` |

### `theme.void.keyboard.shortcuts.tab_left.label`
| | |
|---|---|
| Default | `"Switch to previous tab"` |

### `theme.void.keyboard.shortcuts.tab_right.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.tab_right.key`
| | |
|---|---|
| Default | `"ArrowRight"` |

### `theme.void.keyboard.shortcuts.tab_right.label`
| | |
|---|---|
| Default | `"Switch to next tab"` |

### `theme.void.keyboard.shortcuts.toggle_notes.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_notes.key`
| | |
|---|---|
| Default | `"Ctrl+Shift+N"` |

### `theme.void.keyboard.shortcuts.toggle_notes.label`
| | |
|---|---|
| Default | `"Toggle notes panel"` |

### `theme.void.keyboard.shortcuts.toggle_reading_mode.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_reading_mode.key`
| | |
|---|---|
| Default | `"Alt+Shift+R"` |

### `theme.void.keyboard.shortcuts.toggle_reading_mode.label`
| | |
|---|---|
| Default | `"Toggle reading mode"` |

### `theme.void.keyboard.shortcuts.toggle_reading_mode.persisted`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_repo_popover.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_repo_popover.key`
| | |
|---|---|
| Default | `"Ctrl+Shift+G"` |

### `theme.void.keyboard.shortcuts.toggle_repo_popover.label`
| | |
|---|---|
| Default | `"Toggle repo popover"` |

### `theme.void.keyboard.shortcuts.toggle_scheme.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_scheme.key`
| | |
|---|---|
| Default | `"Ctrl+Shift+L"` |

### `theme.void.keyboard.shortcuts.toggle_scheme.label`
| | |
|---|---|
| Default | `"Toggle color scheme"` |

### `theme.void.keyboard.shortcuts.toggle_sidebar.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_sidebar.key`
| | |
|---|---|
| Default | `"Ctrl+Shift+B"` |
| Purpose | Key that folds/expands the sidebar. |
| Example | `keyboard: {shortcuts: {toggle_sidebar: {key: Ctrl+Shift+B}}}` |

### `theme.void.keyboard.shortcuts.toggle_sidebar.label`
| | |
|---|---|
| Default | `"Toggle sidebar"` |

### `theme.void.keyboard.shortcuts.toggle_sidebar.persisted`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_toc.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.keyboard.shortcuts.toggle_toc.key`
| | |
|---|---|
| Default | `"Ctrl+Shift+T"` |

### `theme.void.keyboard.shortcuts.toggle_toc.label`
| | |
|---|---|
| Default | `"Toggle table of contents"` |

### `theme.void.keyboard.shortcuts.toggle_toc.persisted`
| | |
|---|---|
| Default | `true` |

## reading_mode

- [reading_mode.enabled](#themevoidreading_modeenabled) &middot; [reading_mode.notes.open_on_enter](#themevoidreading_modenotesopen_on_enter) &middot; [reading_mode.notes.show](#themevoidreading_modenotesshow) &middot; [reading_mode.persisted](#themevoidreading_modepersisted) &middot; [reading_mode.sections.footer](#themevoidreading_modesectionsfooter) &middot; [reading_mode.sections.header](#themevoidreading_modesectionsheader) &middot; [reading_mode.sections.progress](#themevoidreading_modesectionsprogress) &middot; [reading_mode.sections.sidebar](#themevoidreading_modesectionssidebar) &middot; [reading_mode.sections.toc](#themevoidreading_modesectionstoc) &middot; [reading_mode.shortcut_key](#themevoidreading_modeshortcut_key) &middot; [reading_mode.typography.font_size](#themevoidreading_modetypographyfont_size) &middot; [reading_mode.typography.line_height](#themevoidreading_modetypographyline_height) &middot; [reading_mode.typography.measure](#themevoidreading_modetypographymeasure)

### `theme.void.reading_mode.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for distraction-free reading mode. |
| Example | `reading_mode: {enabled: true}` |

### `theme.void.reading_mode.notes.open_on_enter`
| | |
|---|---|
| Default | `false` |

### `theme.void.reading_mode.notes.show`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.persisted`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.sections.footer`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.sections.header`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.sections.progress`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.sections.sidebar`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.sections.toc`
| | |
|---|---|
| Default | `true` |

### `theme.void.reading_mode.shortcut_key`
| | |
|---|---|
| Default | `"Alt+Shift+R"` |
| Purpose | Key that enters/leaves reading mode. |
| Example | `reading_mode: {shortcut_key: Alt+Shift+R}` |

### `theme.void.reading_mode.typography.font_size`
| | |
|---|---|
| Default | `"1.125rem"` |

### `theme.void.reading_mode.typography.line_height`
| | |
|---|---|
| Default | `"1.75"` |

### `theme.void.reading_mode.typography.measure`
| | |
|---|---|
| Default | `"100%"` |

## action_cluster

- [action_cluster.actions](#themevoidaction_clusteractions) &middot; [action_cluster.behavior.animation](#themevoidaction_clusterbehavioranimation) &middot; [action_cluster.behavior.close_on_escape](#themevoidaction_clusterbehaviorclose_on_escape) &middot; [action_cluster.behavior.close_on_outside](#themevoidaction_clusterbehaviorclose_on_outside) &middot; [action_cluster.behavior.close_on_select](#themevoidaction_clusterbehaviorclose_on_select) &middot; [action_cluster.behavior.focus_trap](#themevoidaction_clusterbehaviorfocus_trap) &middot; [action_cluster.behavior.min_actions](#themevoidaction_clusterbehaviormin_actions) &middot; [action_cluster.behavior.tooltips](#themevoidaction_clusterbehaviortooltips) &middot; [action_cluster.enabled](#themevoidaction_clusterenabled) &middot; [action_cluster.main.glass](#themevoidaction_clustermainglass) &middot; [action_cluster.main.icon](#themevoidaction_clustermainicon) &middot; [action_cluster.main.icon_transform](#themevoidaction_clustermainicon_transform) &middot; [action_cluster.main.size](#themevoidaction_clustermainsize) &middot; [action_cluster.offset.bottom](#themevoidaction_clusteroffsetbottom) &middot; [action_cluster.offset.left](#themevoidaction_clusteroffsetleft) &middot; [action_cluster.position](#themevoidaction_clusterposition) &middot; [action_cluster.replaces_notes_button](#themevoidaction_clusterreplaces_notes_button)

### `theme.void.action_cluster.actions`
| | |
|---|---|
| Default | `[{badge: none, enabled: true, icon: help, id: keyboard_help, label: Keyboard shortcuts,     shortcut: '?'}, {badge: none, enabled: true, icon: notes, id: notes, label: Open       notes panel, shortcut: Ctrl+Shift+N}, {badge: time, enabled: true, icon: timer,     id: timer, label: Focus timer, shortcut: Alt+Shift+T}, {badge: none, enabled: true,     icon: reading, id: reading_mode, label: Reading mode, shortcut: Alt+Shift+R}]` |

### `theme.void.action_cluster.behavior.animation`
| | |
|---|---|
| Default | `"normal"` |

### `theme.void.action_cluster.behavior.close_on_escape`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.behavior.close_on_outside`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.behavior.close_on_select`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.behavior.focus_trap`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.behavior.min_actions`
| | |
|---|---|
| Default | `2` |

### `theme.void.action_cluster.behavior.tooltips`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the floating plus action cluster. |
| Example | `action_cluster: {enabled: true}` |

### `theme.void.action_cluster.main.glass`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.main.icon`
| | |
|---|---|
| Default | `"plus"` |

### `theme.void.action_cluster.main.icon_transform`
| | |
|---|---|
| Default | `true` |

### `theme.void.action_cluster.main.size`
| | |
|---|---|
| Default | `"44px"` |

### `theme.void.action_cluster.offset.bottom`
| | |
|---|---|
| Default | `"16px"` |

### `theme.void.action_cluster.offset.left`
| | |
|---|---|
| Default | `"16px"` |

### `theme.void.action_cluster.position`
| | |
|---|---|
| Default | `"bottom-left"` |
| Purpose | Which corner the floating cluster pins to. |
| Example | `action_cluster: {position: "bottom-left"}` |

### `theme.void.action_cluster.replaces_notes_button`
| | |
|---|---|
| Default | `true` |

## timer

- [timer.badge_in_cluster](#themevoidtimerbadge_in_cluster) &middot; [timer.colors.progress](#themevoidtimercolorsprogress) &middot; [timer.default_minutes](#themevoidtimerdefault_minutes) &middot; [timer.display_format](#themevoidtimerdisplay_format) &middot; [timer.document_title](#themevoidtimerdocument_title) &middot; [timer.enabled](#themevoidtimerenabled) &middot; [timer.notifications.enabled](#themevoidtimernotificationsenabled) &middot; [timer.notifications.sound](#themevoidtimernotificationssound) &middot; [timer.notifications.toast](#themevoidtimernotificationstoast) &middot; [timer.persist](#themevoidtimerpersist) &middot; [timer.reading.show](#themevoidtimerreadingshow) &middot; [timer.settings_popup](#themevoidtimersettings_popup) &middot; [timer.start_with_reading](#themevoidtimerstart_with_reading) &middot; [timer.toc.position](#themevoidtimertocposition) &middot; [timer.toc.show](#themevoidtimertocshow) &middot; [timer.toc.style](#themevoidtimertocstyle)

### `theme.void.timer.badge_in_cluster`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.colors.progress`
| | |
|---|---|
| Default | `"#8a5a33"` |

### `theme.void.timer.default_minutes`
| | |
|---|---|
| Default | `25` |
| Purpose | Default focus session length in minutes. |
| Example | `timer: {default_minutes: 25}` |

### `theme.void.timer.display_format`
| | |
|---|---|
| Default | `"mm:ss"` |

### `theme.void.timer.document_title`
| | |
|---|---|
| Default | `false` |

### `theme.void.timer.enabled`
| | |
|---|---|
| Default | `true` |
| Purpose | Master switch for the built-in focus timer. |
| Example | `timer: {enabled: true}` |

### `theme.void.timer.notifications.enabled`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.notifications.sound`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.notifications.toast`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.persist`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.reading.show`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.settings_popup`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.start_with_reading`
| | |
|---|---|
| Default | `false` |

### `theme.void.timer.toc.position`
| | |
|---|---|
| Default | `"bottom"` |

### `theme.void.timer.toc.show`
| | |
|---|---|
| Default | `true` |

### `theme.void.timer.toc.style`
| | |
|---|---|
| Default | `"ring"` |

