<!--
name: 'Slash Command: exit worktree changed after check'
description: >-
  Exit result when the worktree was not removed because it changed after Claude
  Code checked it
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_CHANGED_AFTER_CHECK_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_CHANGED_AFTER_CHECK_VAR_1
-->
The exit didn't remove the worktree at ${SLASH_COMMAND_EXIT_WORKTREE_CHANGED_AFTER_CHECK_VAR_0}: this session's worktree changed after Claude Code checked it.${SLASH_COMMAND_EXIT_WORKTREE_CHANGED_AFTER_CHECK_VAR_1?" Tmux session ended.":""}
