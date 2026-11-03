<!--
name: 'Tool Result: Bash worktree isolation rsync remote shell'
description: >-
  Refusal reason: rsync is handed a remote shell it splits itself, so it cannot
  be shown not to be git; lists the allowed characters
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_2
-->
hands ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_0} the remote shell ${TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_1(TOOL_RESULT_BASH_WORKTREE_ISOLATION_RSYNC_REMOTE_SHELL_VAR_2)}, which rsync splits into words itself, with no shell, so what it runs cannot be shown not to be git (to pass, use only ASCII letters, digits, spaces, undoubled quotes and _ . , : / = + @ % ^ ~ -, with ~ only as ~/ at the start or after a : or =)
