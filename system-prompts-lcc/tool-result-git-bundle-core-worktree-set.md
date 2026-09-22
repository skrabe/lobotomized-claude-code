<!--
name: 'Tool Result: Git Bundle core.worktree Set'
description: >-
  Refuses the hardened git-bundle upload when git resolves this checkout's
  working tree to another directory via core.worktree.
ccVersion: 2.1.246
-->
Not uploading this working tree: git resolves this checkout’s working tree to another directory (core.worktree is set), which this upload does not support yet. Start from an ordinary clone of the repository instead, or unset core.worktree if nothing here relies on it.
