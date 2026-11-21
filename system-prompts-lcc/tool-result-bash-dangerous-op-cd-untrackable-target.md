<!--
name: 'Tool Result: dangerous op target after untrackable cd'
description: >-
  Ask message when directory changes in the command make the removal target
  unknowable
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_CD_UNTRACKABLE_TARGET_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_CD_UNTRACKABLE_TARGET_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_CD_UNTRACKABLE_TARGET_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_CD_UNTRACKABLE_TARGET_VAR_1}'

Claude Code can't follow the directory changes in this command, so it can't tell what that target would remove. This requires explicit approval and cannot be auto-allowed by permission rules.
