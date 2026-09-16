<!--
name: 'Tool Result: Bash dangerous operation — target not resolvable to a directory'
description: >-
  Refusal the model reads when a destructive bash command's removal target
  cannot be statically resolved to a directory; it states the action needs
  explicit approval and cannot be auto-allowed by a permission rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_TARGET_NOT_RESOLVABLE_TO_DIRECTORY_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_TARGET_NOT_RESOLVABLE_TO_DIRECTORY_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_TARGET_NOT_RESOLVABLE_TO_DIRECTORY_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_TARGET_NOT_RESOLVABLE_TO_DIRECTORY_VAR_1}'

This command's removal target cannot be statically resolved to a directory. This requires explicit approval and cannot be auto-allowed by permission rules.
