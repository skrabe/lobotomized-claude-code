<!--
name: 'Tool Result: Bash dangerous operation — relative glob unresolvable'
description: >-
  Refusal the model reads when a destructive bash command changes directories
  before the removal, so its relative glob target cannot be statically resolved;
  it states the action needs explicit approval and cannot be auto-allowed by a
  permission rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_1}'

This command changes directories before the removal, so the relative glob target cannot be statically resolved. This requires explicit approval and cannot be auto-allowed by permission rules.
