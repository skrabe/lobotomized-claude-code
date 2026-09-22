<!--
name: 'Tool Result: Async Agent Running (send message)'
description: >-
  Tells the model a background agent is still running without an output file: do
  not spawn a duplicate; send it a message for a progress report.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0
-->
Do NOT spawn a duplicate. You will be notified when it completes. Send it a message with ${TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0} if you need a progress report before then.
