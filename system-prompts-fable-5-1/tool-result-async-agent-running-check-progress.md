<!--
name: 'Tool Result: Async Agent Running (check progress)'
description: >-
  Tool_result note when a spawned async agent is still running without an output
  file: do not spawn a duplicate; check progress or message it.
ccVersion: 2.1.178
variables:
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_CHECK_PROGRESS_VAR_0
  - TOOL_RESULT_ASYNC_AGENT_RUNNING_CHECK_PROGRESS_VAR_1
-->
An instance is already running; don't spawn a duplicate. You'll be notified when it completes. Read partial output at ${TOOL_RESULT_ASYNC_AGENT_RUNNING_CHECK_PROGRESS_VAR_0.outputFilePath} or message it with ${TOOL_RESULT_ASYNC_AGENT_RUNNING_CHECK_PROGRESS_VAR_1}.
