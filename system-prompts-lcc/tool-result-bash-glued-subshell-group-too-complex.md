<!--
name: 'Tool Result: Bash Glued Subshell Group Too Complex'
description: >-
  Too-complex reason when a ( … ) group is glued to a preceding statement, which
  zsh would glob-expand.
ccVersion: 2.1.273
-->
`(…)` group directly follows a statement or word on the same line — bash rejects the line, but zsh reads the glued `(…)` as a glob-group word and expands what follows it
