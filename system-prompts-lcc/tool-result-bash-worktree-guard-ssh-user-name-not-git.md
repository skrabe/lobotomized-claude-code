<!--
name: 'Tool Result: Bash worktree guard ssh user name'
description: >-
  Refuses an ssh user name that a ProxyCommand could paste into a shell and
  lists the characters a passing user name must avoid
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_2
-->
hands ${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_0} the user name ${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_1(TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_USER_NAME_NOT_GIT_VAR_2)}, which ssh pastes into a shell command if a ProxyCommand in an ssh config file uses it, so what it runs cannot be shown not to be git (to pass, use a user name with no leading -, no trailing \\, no whitespace and none of ' " \` $ ; & | < > ( ) { } * ? [ ] ! # %, and no + in an sftp:// address)
