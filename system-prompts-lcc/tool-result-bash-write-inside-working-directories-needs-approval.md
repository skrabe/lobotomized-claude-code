<!--
name: 'Tool Result: Bash write inside working directories needs approval'
description: >-
  Permission ask message for a shell command that would create, change or remove
  files at a path inside the session's working directories.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_WRITE_INSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_0
  - TOOL_RESULT_BASH_WRITE_INSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_1
-->
${TOOL_RESULT_BASH_WRITE_INSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_0} needs approval. The path is inside the working directories for this session (${TOOL_RESULT_BASH_WRITE_INSIDE_WORKING_DIRECTORIES_NEEDS_APPROVAL_VAR_1}), and Claude Code asks before a shell command creates, changes or removes files there.
