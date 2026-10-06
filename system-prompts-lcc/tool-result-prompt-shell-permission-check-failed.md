<!--
name: 'Tool Result: prompt shell permission check failed'
description: >-
  Skill/command shell substitution error when the permission check denies the
  command.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_PROMPT_SHELL_PERMISSION_CHECK_FAILED_VAR_0
  - TOOL_RESULT_PROMPT_SHELL_PERMISSION_CHECK_FAILED_VAR_1
-->
Shell command permission check failed for pattern "${TOOL_RESULT_PROMPT_SHELL_PERMISSION_CHECK_FAILED_VAR_0}": ${TOOL_RESULT_PROMPT_SHELL_PERMISSION_CHECK_FAILED_VAR_1.message||"Permission denied"}
