<!--
name: 'Tool Result: Bash Case Pattern Comment Too Complex'
description: >-
  Too-complex reason when a case pattern group holds a comment that zsh would
  expand as a glob word.
ccVersion: 2.1.273
-->
`case` pattern group holds a comment — bash reads no comment inside a pattern list, but zsh reads the group as one glob word and expands its contents
