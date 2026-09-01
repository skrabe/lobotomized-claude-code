<!--
name: 'Tool Result: Async Agent Running (read partial output)'
description: >-
  Tool_result note when a spawned async agent is still running and has an output
  file: do not spawn a duplicate; read partial output or message it.
ccVersion: 2.1.178
variables:
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_1
-->
Do NOT spawn a duplicate. You will be notified when it completes. You can check its progress with the ${TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0} tool or send it a message with ${TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_1}.
