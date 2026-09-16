<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable inside command
  substitution
description: >-
  Refusal the model reads when a destructive bash command inside a command
  substitution targets a shell variable expansion that resolves to the
  filesystem root or a top-level directory when unset or empty; it states the
  action needs explicit approval and cannot be auto-allowed by a permission
  rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_IN_COMMAND_SUBSTITUTION_VAR_0
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_IN_COMMAND_SUBSTITUTION_VAR_0.command} operation detected inside command substitution: '${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_IN_COMMAND_SUBSTITUTION_VAR_0.target}'

This target is a shell variable expansion that points at the filesystem root (or a top-level directory) when the variable is unset or empty. This requires explicit approval and cannot be auto-allowed by permission rules.
