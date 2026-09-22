<!--
name: 'Tool Result: Bash Comment Glued To Paren Too Complex'
description: >-
  Bash permission-check too-complex reason when a comment is glued to a paren,
  because zsh would treat the glued group as a glob that executes.
ccVersion: 2.1.273
-->
comment glued to a paren — bash reads `)#…` and `(#…` as a comment, but zsh reads a keyword- or word-glued `(…)` as a glob group whose `#…` text is word content that executes
