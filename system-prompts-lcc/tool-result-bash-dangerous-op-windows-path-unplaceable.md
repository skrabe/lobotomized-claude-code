<!--
name: 'Tool Result: Bash dangerous op Windows path unplaceable'
description: >-
  Permission ask message when an rm/rmdir target is a Windows path the safety
  check cannot place under Git Bash
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_WINDOWS_PATH_UNPLACEABLE_VAR_1}'

Git Bash may read this Windows path differently from this check, so where it lands is unknown. This requires explicit approval and cannot be auto-allowed by permission rules.

Write the directory you mean as a plain path, for example /c/work/build or C:/work/build.
