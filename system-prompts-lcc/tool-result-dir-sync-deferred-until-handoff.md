<!--
name: 'Tool Result: Dir Sync Deferred Until Handoff'
description: >-
  After-forward sessionNote when the host sent post-command files that are only
  written here after the task hands back to the main conversation.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_DIR_SYNC_DEFERRED_UNTIL_HANDOFF_VAR_0
  - TOOL_RESULT_DIR_SYNC_DEFERRED_UNTIL_HANDOFF_VAR_1
-->
Directory sync: ${TOOL_RESULT_DIR_SYNC_DEFERRED_UNTIL_HANDOFF_VAR_0} sent what that command changed, but those files are written here only after this task hands back to the main conversation — to read them now, read them on ${TOOL_RESULT_DIR_SYNC_DEFERRED_UNTIL_HANDOFF_VAR_0} (the ${TOOL_RESULT_DIR_SYNC_DEFERRED_UNTIL_HANDOFF_VAR_1} argument).
