<!--
name: 'Tool Result: Read Symlink Resolution Changed After Permission'
description: >-
  Refuses a read when symlink resolution changed after the permission check and
  tells the model to stop concurrent rewrites and retry.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_0
  - TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_1
-->
Refusing to read ${TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_0}: its symlink resolution changed after permission was checked (${TOOL_RESULT_READ_SYMLINK_RESOLUTION_CHANGED_AFTER_PERMISSION_VAR_1[r]}). If a link in the working directory is being rewritten concurrently, stop that and retry.
