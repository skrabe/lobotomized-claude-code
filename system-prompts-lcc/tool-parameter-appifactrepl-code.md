<!--
name: 'Tool Parameter: AppifactRepl code'
description: >-
  Input-schema description of AppifactRepl.code: plain JavaScript for the SDK
  REPL, with invisible-character escaping rules for the approval dialog.
ccVersion: 2.1.273
-->
Plain JavaScript for the SDK REPL: top-level statements, each on its own line or lines, run in order in one shared scope. The code is approved by reading, so it carries no invisible character raw: use emoji without joiners or variation selectors (single code points: 👩 🍳 ❤ rather than 👩‍🍳 ❤️), or write such a sequence as escapes inside a string ("\u{1F469}\u200D\u{1F373}", "\u2764\uFE0F"); a zero-width space or other format character goes in as a \u escape too.
