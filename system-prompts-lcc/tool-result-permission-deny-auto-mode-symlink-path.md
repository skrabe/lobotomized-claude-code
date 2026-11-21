<!--
name: 'Tool result: Permission deny auto mode symlink path'
description: >-
  Auto mode denial asking to repeat the write with the real path instead of a
  symlinked one
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_0
  - TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_1
  - TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_2
-->
${TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_0(TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_1)} goes through a symlink. Auto mode needs the real path: make the same call with ${TOOL_RESULT_PERMISSION_DENY_AUTO_MODE_SYMLINK_PATH_VAR_2}.
