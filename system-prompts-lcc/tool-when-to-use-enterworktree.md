<!--
name: 'Tool whenToUse: EnterWorktree'
description: >-
  EnterWorktree whenToUse line: when user or project instructions say to work in
  a worktree; plain branch work uses git
ccVersion: 2.1.330
variables:
  - TOOL_WHEN_TO_USE_ENTERWORKTREE_VAR_0
-->
When the user or the project's instructions have said to work in a worktree and you are about to begin, use it; for plain branch work use ${TOOL_WHEN_TO_USE_ENTERWORKTREE_VAR_0("session")?"version control":"git"} and not this.
