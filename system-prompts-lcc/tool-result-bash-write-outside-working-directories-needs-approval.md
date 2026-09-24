<!--
name: 'Tool Result: Bash write outside working directories needs approval'
description: >-
  Permission ask message for a shell command that targets a path outside the
  session's working directories. Allowing it runs the command as written.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_WRITE_OUTSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_0
  - TOOL_RESULT_BASH_WRITE_OUTSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_1
-->
${TOOL_RESULT_BASH_WRITE_OUTSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_0} needs approval. The path is outside the working directories for this session (${TOOL_RESULT_BASH_WRITE_OUTSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_1}). Allowing runs the command as written.
