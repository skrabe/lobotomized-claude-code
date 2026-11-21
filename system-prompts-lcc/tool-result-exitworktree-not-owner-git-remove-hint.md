<!--
name: 'Tool Result: ExitWorktree not-owner git remove hint'
description: >-
  Tells Claude it may remove the worktree with git worktree remove if no other
  session uses it
ccVersion: 2.1.330
-->
If no other session is using it, remove it yourself with `git worktree remove`; while a live session's lock is present, git will refuse and name the owner.
