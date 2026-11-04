<!--
name: 'Tool Result: Bash worktree guard ssh command option not plain'
description: >-
  Refuses an ssh option setting a command such as ProxyCommand that is not plain
  words
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_1
  - TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_2
-->
${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_0(`${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_1} ${TOOL_RESULT_BASH_WORKTREE_GUARD_SSH_COMMAND_OPTION_NOT_PLAIN_VAR_2}`,"with a program that sets a command (such as ProxyCommand) and holds more than plain words, which this check cannot follow")}; write that command in plain words, with the host and user spelled out
