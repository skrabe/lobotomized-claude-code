<!--
name: Remote Host Still Running Await Result
description: >-
  Remote-tool error telling the model the host still has the command running and
  not to repeat it.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_0
  - TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_1
-->
${TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_0(TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_1.host)}; ${TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_1.host} reports it is still running there, and its result has not reached this session yet. Do not repeat it — check its effect on ${TOOL_RESULT_REMOTE_HOST_STILL_RUNNING_AWAIT_RESULT_VAR_1.host} first.
