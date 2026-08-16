<!--
name: 'Tool Result: Notebook outputs too large — POSIX recovery command'
description: >-
  The `cat | jq` command offered to the model for reading an individual notebook
  cell whose outputs were too large to return.
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POSIX_RECOVERY_VAR_0
  - TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POSIX_RECOVERY_VAR_1
-->
${TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POSIX_RECOVERY_VAR_0} with: cat <notebook_path> | jq '.cells[${TOOL_RESULT_NOTEBOOK_OUTPUTS_TOO_LARGE_POSIX_RECOVERY_VAR_1}].outputs'
