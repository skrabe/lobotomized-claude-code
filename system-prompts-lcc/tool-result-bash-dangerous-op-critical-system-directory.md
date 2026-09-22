<!--
name: 'Tool Result: Bash dangerous operation — critical system directory'
description: >-
  Refusal the model reads when a destructive bash command would remove a
  critical system directory; it states the action needs explicit approval and
  cannot be auto-allowed by a permission rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_CRITICAL_SYSTEM_DIRECTORY_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_CRITICAL_SYSTEM_DIRECTORY_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_CRITICAL_SYSTEM_DIRECTORY_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_CRITICAL_SYSTEM_DIRECTORY_VAR_1}'

This command would remove a critical system directory. This requires explicit approval and cannot be auto-allowed by permission rules.
