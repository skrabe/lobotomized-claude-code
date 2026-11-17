<!--
name: >-
  Slash Command: Exit Worktree — detached tmux session may still be running,
  kill it
description: >-
  Warns that the worktree's detached tmux session may still be running and gives
  the tmux kill-session command to end it.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_INACCESSIBLE_TMUX_STILL_RUNNING_VAR_0
-->
. Detached tmux session ${SLASH_COMMAND_EXIT_WORKTREE_INACCESSIBLE_TMUX_STILL_RUNNING_VAR_0.tmuxSessionName} may still be running. Stop it with: tmux kill-session -t ${SLASH_COMMAND_EXIT_WORKTREE_INACCESSIBLE_TMUX_STILL_RUNNING_VAR_0.tmuxSessionName}
