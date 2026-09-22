<!--
name: AppifactRepl Input Contains Emoji Joiner Or Variation Selector
description: >-
  AppifactRepl input-schema refine error when skill/artifact/code contains
  U+200D or U+FE0F that the approval dialog would hide.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_APPIFACT_REPL_EMOJI_JOINER_OR_VARIATION_SELECTOR_VAR_0
-->
input contains an emoji joiner or variation selector (U+${TOOL_RESULT_APPIFACT_REPL_EMOJI_JOINER_OR_VARIATION_SELECTOR_VAR_0.padStart(4,"0")}) that the approval dialog would not show; use emoji without joiners or variation selectors (single code points, e.g. 👩 🍳 ❤), or write the whole sequence as escapes inside a string (e.g. "\\u{1F469}\\u200D\\u{1F373}")
