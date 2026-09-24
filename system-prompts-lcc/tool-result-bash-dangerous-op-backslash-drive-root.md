<!--
name: 'Tool Result: bash dangerous op backslash drive root'
description: >-
  Permission-ask message for an rm/rmdir whose target is only backslashes (the
  drive root in Git Bash on Windows): it needs explicit approval, and the model
  should write the directory as a real path.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_BACKSLASH_DRIVE_ROOT_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_BACKSLASH_DRIVE_ROOT_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_BACKSLASH_DRIVE_ROOT_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_BACKSLASH_DRIVE_ROOT_VAR_1}'

A backslash-only target is the drive root in Git Bash on Windows. This requires explicit approval and cannot be auto-allowed by permission rules.

Write the directory you mean as a path, for example /c/work/build or C:/work/build.
