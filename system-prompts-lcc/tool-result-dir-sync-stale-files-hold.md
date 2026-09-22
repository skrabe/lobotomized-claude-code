<!--
name: 'Tool Result: Dir Sync Stale Files Hold'
description: >-
  sync_failed tool_result when a mutating command is held because it would have
  acted on stale host files.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_0
  - TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_1
  - TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_2
-->
Not run on ${TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_0}: ${TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_1}, so the command would have acted on stale files. ${TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_0} was not contacted. What clears it: ${TOOL_RESULT_DIR_SYNC_STALE_FILES_HOLD_VAR_2}.
