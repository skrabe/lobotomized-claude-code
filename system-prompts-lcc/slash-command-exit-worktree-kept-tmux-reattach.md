<!--
name: 'Slash Command: Exit Worktree Kept Tmux Reattach'
description: >-
  /exit output when the user keeps both the worktree and its tmux session: gives
  the saved worktree path and the tmux attach command to reattach.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_TMUX_REATTACH_VAR_0
  - SLASH_COMMAND_EXIT_WORKTREE_KEPT_TMUX_REATTACH_VAR_1
-->
Worktree kept. Your work is saved at ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_TMUX_REATTACH_VAR_0.worktreePath}${SLASH_COMMAND_EXIT_WORKTREE_KEPT_TMUX_REATTACH_VAR_1}. Reattach to tmux session with: tmux attach -t ${SLASH_COMMAND_EXIT_WORKTREE_KEPT_TMUX_REATTACH_VAR_0.tmuxSessionName}
