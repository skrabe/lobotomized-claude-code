<!--
name: 'Tool Result: Bash worktree guard ssh %r without user'
description: Refuses %r with no user per host and asks to write the user out as user@host
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_PERCENT_R_NO_USER_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_PERCENT_R_NO_USER_VAR_1
-->
${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_PERCENT_R_NO_USER_VAR_0(TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_PERCENT_R_NO_USER_VAR_1,"with %r and no user written for each host (-o User does not count)")}; ssh may fill %r from a config file this check does not read (a line there reading User git makes %r git), so write the user out, as user@host
