<!--
name: 'Tool Result: Bash Function Parenthesised Body Too Complex'
description: >-
  Too-complex reason for a function with a parenthesised body and no (), which
  zsh reads as a glob-group word.
ccVersion: 2.1.273
-->
`function` with a parenthesised body and no `()` — bash reads a subshell body, but zsh reads one glob-group word and expands its contents
