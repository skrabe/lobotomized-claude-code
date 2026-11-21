<!--
name: 'Tool Result: dangerous op relative glob after cd'
description: >-
  Ask message when a command changes directories and the target is a relative
  glob
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_RELATIVE_GLOB_UNRESOLVABLE_VAR_1}'

This command also changes directories, so this relative glob target requires explicit approval and cannot be auto-allowed by permission rules.
