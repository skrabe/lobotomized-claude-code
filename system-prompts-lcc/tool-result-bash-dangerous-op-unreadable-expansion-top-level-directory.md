<!--
name: >-
  Tool Result: Bash dangerous operation — unreadable expansion ending in a
  top-level directory
description: >-
  Dangerous-removal ask message for a target that starts with a shell expansion
  the check cannot read and ends in a top-level directory name, so an empty
  expansion would remove that directory.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_2
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_1}'

The target starts with a shell expansion this check cannot read and ends in a top-level directory name: if the expansion is empty, this removes '/${TOOL_RESULT_BASH_DANGEROUS_OP_UNREADABLE_EXPANSION_TOP_LEVEL_DIRECTORY_VAR_2}'. This requires explicit approval and cannot be auto-allowed by permission rules.

Use a literal absolute path instead.
