<!--
name: 'Tool result: MCP tool backgrounded notification suffix'
description: >-
  Suffix telling the model it will be notified on completion, can keep working,
  how to stop it with TaskStop, and that it does not survive exit
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_MCP_TOOL_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_0
-->
; you'll receive a notification with the result when it completes. You can keep working in the meantime. To stop it, use TaskStop with task_id "${TOOL_RESULT_MCP_TOOL_BACKGROUNDED_NOTIFICATION_SUFFIX_VAR_0}". It does not survive exiting this session.
