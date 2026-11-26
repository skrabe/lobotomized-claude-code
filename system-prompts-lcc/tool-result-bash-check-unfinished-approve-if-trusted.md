<!--
name: 'Tool Result: Bash check unfinished, approve if trusted'
description: >-
  Permission reason: Claude Code couldn't finish checking a command, or the
  command sets a variable that can make git run a program; approve only if
  trusted.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_BASH_CHECK_UNFINISHED_APPROVE_IF_TRUSTED_VAR_0
  - TOOL_RESULT_BASH_CHECK_UNFINISHED_APPROVE_IF_TRUSTED_VAR_1
-->
${TOOL_RESULT_BASH_CHECK_UNFINISHED_APPROVE_IF_TRUSTED_VAR_0?"Claude Code couldn't finish checking this command.":"This command sets a variable that can make git run a program."} ${TOOL_RESULT_BASH_CHECK_UNFINISHED_APPROVE_IF_TRUSTED_VAR_1===void 0?"":`${TOOL_RESULT_BASH_CHECK_UNFINISHED_APPROVE_IF_TRUSTED_VAR_1.reason} `}Approve only if you trust it.
