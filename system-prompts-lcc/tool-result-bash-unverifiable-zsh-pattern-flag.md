<!--
name: 'Tool result: Bash zsh pattern flag unverifiable'
description: >-
  Permission ask reason when $ followed by ~ may make zsh treat a value as a
  pattern.
ccVersion: 2.1.325
-->
A $ followed by ~ in this command may make zsh read a value as a pattern, which may run code that can't be checked before it runs
