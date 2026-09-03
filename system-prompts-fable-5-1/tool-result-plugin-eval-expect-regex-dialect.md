<!--
name: 'Tool Result: Plugin Eval Expect Regex Dialect'
description: >-
  Mock MCP abort text when an expect: /regex/ guard uses groups, alternation,
  backreferences, or lookaround.
ccVersion: 2.1.246
-->
expect: /regex/ guards use a small dialect — literals, ".", escapes, character classes, and quantifiers (* + ? {m,n}) on single atoms, with optional ^ and $; no groups "(…)", alternation "|", backreferences, or lookaround. Use a list of literals, a type name, or several simpler guards instead
