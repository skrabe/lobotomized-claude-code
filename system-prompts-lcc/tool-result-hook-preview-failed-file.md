<!--
name: Hook file-preview denial
description: >-
  Deny reason returned to the model when a PermissionRequest hook changed a file
  call and Claude Code could not rebuild the permission prompt for the changed
  call, so the call was not run.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_0
-->
A PermissionRequest hook changed this call, and Claude Code could not build a permission prompt for the changed call${TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_0===void 0?"":` (${TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_0})`}, so it was not run. Tell the user.
