<!--
name: Path Outside Working Directories Read Block Ask
description: >-
  Permission-ask when ln/cp/mv (and the PowerShell sibling) name a path outside
  working directories under the read block.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_PATH_OUTSIDE_WORKING_DIRECTORIES_READ_BLOCK_ASK_VAR_0
-->
${TOOL_RESULT_PATH_OUTSIDE_WORKING_DIRECTORIES_READ_BLOCK_ASK_VAR_0} names a path outside the working directories, which the read block does not allow without asking (permissions.blockReadsOutsideWorkingDirectories). Add the directory with /add-dir, or remove that setting.
