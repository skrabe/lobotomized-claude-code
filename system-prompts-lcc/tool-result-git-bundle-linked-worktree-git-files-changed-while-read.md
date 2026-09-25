<!--
name: 'Tool result: git bundle linked worktree git files changed while read'
description: >-
  Upload failure when a linked worktree's git files in .git changed while being
  read.
ccVersion: 2.1.282
-->
This linked worktree’s git files, in its repository’s .git directory, changed while they were being read (removed, moved or replaced meanwhile), so nothing was uploaded. Retry; if it keeps happening, check what else is changing that .git directory.
