<!--
name: 'Tool Result: Bash script call limit exceeded'
description: >-
  Error returned when a command invokes a capped script more times than
  CLAUDE_CODE_SCRIPT_CAPS allows in an untrusted-input workflow.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_0
  - TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_1
  - TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_2
-->
Script call limit exceeded: ${TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_0} has been called ${TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_1} times (cap: ${TOOL_RESULT_BASH_SCRIPT_CALL_LIMIT_EXCEEDED_VAR_2}). This limit prevents data exfiltration via repeated write operations in untrusted-input workflows.
