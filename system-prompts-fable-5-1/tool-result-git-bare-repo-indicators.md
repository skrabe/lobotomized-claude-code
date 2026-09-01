<!--
name: Git in a bare-repo-indicator directory
description: >-
  Command-safety approval reason surfaced to the model when git runs where
  bare-repo indicators may cause hook execution.
ccVersion: 2.1.206
-->
Git command in a directory with bare-repo indicators (HEAD/objects/refs outside a .git/ directory). Git may treat it as a git dir and run config/hooks from here.
