<!--
name: 'Tool Result: Dir Sync Push Failed'
description: >-
  After-forward sessionNote when the host could not send what that command
  changed.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_DIR_SYNC_PUSH_FAILED_VAR_0
  - TOOL_RESULT_DIR_SYNC_PUSH_FAILED_VAR_1
-->
Directory sync: ${TOOL_RESULT_DIR_SYNC_PUSH_FAILED_VAR_0} could not send what that command changed (${TOOL_RESULT_DIR_SYNC_PUSH_FAILED_VAR_1.reason.replace(/_/g," ")}); files it changed there reach this session with the user's next message.
