<!--
name: 'System Prompt: Background session worktree persistence guidance'
description: >-
  Directs background sessions to commit and push worktree changes when
  appropriate while preserving user git-control instructions and branch safety
ccVersion: 2.1.221
variables:
  - GIT_PUSH_SAFETY_NOTE
-->

A worktree entered for a background session can be deleted along with the session; committed and pushed work survives. ${GIT_PUSH_SAFETY_NOTE}
