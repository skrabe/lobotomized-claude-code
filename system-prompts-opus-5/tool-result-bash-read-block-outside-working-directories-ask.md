<!--
name: 'Tool Result: Bash Read Block Outside Working Directories Ask'
description: >-
  Permission-ask message when a command names a path outside working directories
  under permissions.blockReadsOutsideWorkingDirectories.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_BASH_READ_BLOCK_OUTSIDE_WORKING_DIRECTORIES_ASK_VAR_0
  - TOOL_RESULT_BASH_READ_BLOCK_OUTSIDE_WORKING_DIRECTORIES_ASK_VAR_1
-->
${TOOL_RESULT_BASH_READ_BLOCK_OUTSIDE_WORKING_DIRECTORIES_ASK_VAR_0} names '${TOOL_RESULT_BASH_READ_BLOCK_OUTSIDE_WORKING_DIRECTORIES_ASK_VAR_1.resolvedPath}', outside the working directories, which the read block does not allow without asking (permissions.blockReadsOutsideWorkingDirectories). Add the directory with /add-dir, or remove that setting.
