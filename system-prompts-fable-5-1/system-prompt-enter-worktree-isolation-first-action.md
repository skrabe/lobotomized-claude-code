<!--
name: 'System Prompt: EnterWorktree isolation first action'
description: >-
  agent directive to call EnterWorktree as the first action under isolation:
  worktree
ccVersion: 2.1.178
-->
This agent is configured with `isolation: worktree`. Call the EnterWorktree tool as your first action — before reading files or running commands — unless your cwd is already under `.claude/worktrees/`. If EnterWorktree fails, continue in place.
