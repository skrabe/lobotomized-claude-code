<!--
name: EnterWorktree cwd guidance
description: >-
  Continuation of the EnterWorktree error advising the model to use path or
  spawn an Agent with cwd.
ccVersion: 2.1.206
-->
To switch this agent into an existing worktree managed by Claude Code (under .claude/worktrees/ of this repository), call EnterWorktree with `path`. To work in any other directory, spawn an Agent with `cwd` set to it.
