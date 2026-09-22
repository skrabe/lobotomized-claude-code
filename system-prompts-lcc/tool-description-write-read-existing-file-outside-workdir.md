<!--
name: 'Tool Description: Write Read Existing File Outside Working Directory'
description: >-
  Write-tool description fragment requiring a Read of an existing file outside
  the working directory before overwriting it.
ccVersion: 2.1.237
variables:
  - TOOL_DESCRIPTION_WRITE_READ_EXISTING_FILE_OUTSIDE_WORKDIR_VAR_0
-->

- If this is an existing file outside the working directory, you MUST use the ${TOOL_DESCRIPTION_WRITE_READ_EXISTING_FILE_OUTSIDE_WORKDIR_VAR_0} tool first to read the file's contents. This tool will fail if you did not.
