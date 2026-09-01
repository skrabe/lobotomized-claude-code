<!--
name: Hook file-preview denial
description: >-
  cancelAndAbort denial reason returned to the model when a hook-rewritten file
  op cannot be previewed.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_0
  - TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_1
-->
Failed to preview the hook-rewritten file operation: ${TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_0(TOOL_RESULT_HOOK_PREVIEW_FAILED_FILE_VAR_1)}
