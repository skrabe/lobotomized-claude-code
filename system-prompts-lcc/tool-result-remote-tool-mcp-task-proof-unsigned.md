<!--
name: 'Tool Result: remote tool MCP task proof unsigned'
description: >-
  Remote tool result when an MCP tool started a background task but the target
  machine could not sign the proof needed to follow it, so the task is cancelled
  and a retry may work.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_MCP_TASK_PROOF_UNSIGNED_VAR_0
-->
The tool started a background task on ${TOOL_RESULT_REMOTE_TOOL_MCP_TASK_PROOF_UNSIGNED_VAR_0.targetName}, but ${TOOL_RESULT_REMOTE_TOOL_MCP_TASK_PROOF_UNSIGNED_VAR_0.targetName} could not sign the proof that this chat needs to follow that task, so it is cancelling the task. Nothing more of it will arrive. Running the call again may work.
