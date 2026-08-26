<!--
name: 'Remote Tool: Host Ask Unanswerable, No Audience'
description: >-
  insteadOfRejection tool_result when the host asked and this session had no way
  to put the question to anyone; tells the model to ask the user rather than
  retry.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_ASK_UNANSWERABLE_NO_AUDIENCE_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_ASK_UNANSWERABLE_NO_AUDIENCE_VAR_0.host.name} asked before running this call and this session had no way to put the question to anyone; the call was not run. Ask the user how to proceed rather than retrying.
