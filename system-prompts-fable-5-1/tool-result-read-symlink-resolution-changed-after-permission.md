<!--
name: 'Tool Result: Read Symlink Resolution Changed After Permission'
description: >-
  Read tool refusal when a file's symlink resolution changed between the
  permission check and the read, with the specific reason and advice to stop
  concurrent link rewrites and retry
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_0
  - TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_1
-->
Refusing to read ${TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_0}: its symlink resolution changed after permission was checked (${TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_1[a]}). If a link in the working directory is being rewritten concurrently, stop that and retry.
