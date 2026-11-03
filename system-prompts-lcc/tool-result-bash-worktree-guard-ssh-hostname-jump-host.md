<!--
name: 'Tool Result: Bash worktree guard ssh HostName via jump host'
description: >-
  Names a HostName or destination host that ssh pastes into a shell command when
  connecting through a jump host
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_2
-->
the ${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_0?"HostName":"destination host"} ${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_1(TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_HOSTNAME_JUMP_HOST_VAR_2)}, which ssh pastes into a shell command when it connects through a jump host (given here or in an ssh config file)
