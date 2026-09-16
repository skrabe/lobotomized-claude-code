<!--
name: 'Tool Result: Bash dangerous operation — unset variable expansion (lead)'
description: >-
  Opening fragment of the refusal the model reads when a destructive bash
  command's target is a shell variable expansion; names the operation and the
  offending target.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_LEAD_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_LEAD_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_LEAD_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_LEAD_VAR_1}'

This target is a shell variable expansion that points at the filesystem 
