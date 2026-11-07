<!--
name: 'Tool Result: File write pre-read failed'
description: >-
  Deny message when Claude Code could not read the file a write would replace,
  so nothing was written and no prompt shown; retry may fail, tell the user.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_FILE_WRITE_PREREAD_FAILED_NO_PROMPT_VAR_0
  - TOOL_RESULT_FILE_WRITE_PREREAD_FAILED_NO_PROMPT_VAR_1
-->
Claude Code could not read the file that this call would write (${TOOL_RESULT_FILE_WRITE_PREREAD_FAILED_NO_PROMPT_VAR_0}). Nothing was written, and no permission prompt was shown. ${TOOL_RESULT_FILE_WRITE_PREREAD_FAILED_NO_PROMPT_VAR_1} reads a file before replacing it, so a retry may fail the same way; if it does, tell the user.
