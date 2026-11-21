<!--
name: 'Tool Result: dangerous op Windows path unplaceable'
description: Ask message when Git Bash may read a Windows path differently
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_2
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_1(TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_2)}'

Git Bash may read this Windows path differently from this check, so where it lands is unknown. This requires explicit approval and cannot be auto-allowed by permission rules.

Write the directory you mean as a plain path, for example /c/work/build or C:/work/build.
