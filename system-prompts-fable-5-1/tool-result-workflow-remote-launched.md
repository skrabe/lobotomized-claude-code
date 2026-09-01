<!--
name: 'Workflow tool result: remote CCR launch'
description: >-
  tool_result content returned to the model when a workflow launches in a remote
  CCR session, reporting task ID and session URL; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_WORKFLOW_REMOTE_LAUNCHED_VAR_0
-->
Workflow launched in a remote CCR session. Task ID: ${TOOL_RESULT_WORKFLOW_REMOTE_LAUNCHED_VAR_0.taskId}
Session: ${TOOL_RESULT_WORKFLOW_REMOTE_LAUNCHED_VAR_0.sessionUrl}
