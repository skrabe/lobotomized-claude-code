<!--
name: Running Agent Duplicate Warning
description: >-
  Warns against duplicating a running agent and offers a progress request when
  supported.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_1
-->
Do NOT spawn a duplicate. You will be notified when it completes.${TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_0?` Send it a message with ${TOOL_RESULT_ASYNC_AGENT_RUNNING_READ_PARTIAL_VAR_1} if you need a progress report before then.`:""}
