<!--
name: 'Tool Result: Bash dangerous operation — workspace directory'
description: >-
  Refusal the model reads when a destructive bash command would remove the
  working directory, an additional working directory, or a parent of either; it
  states the action needs explicit approval and cannot be auto-allowed by a
  permission rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_WORKSPACE_DIRECTORY_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_WORKSPACE_DIRECTORY_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_WORKSPACE_DIRECTORY_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_WORKSPACE_DIRECTORY_VAR_1}'

This command would remove a workspace directory (the working directory, an additional working directory, or one of their parent directories). This requires explicit approval and cannot be auto-allowed by permission rules.
