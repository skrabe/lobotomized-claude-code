<!--
name: 'Remote Tool: Unanswerable Prompt, Call Did Not Run'
description: >-
  Error tool_result when the session permission prompt is unanswerable,
  appending that the call did not run on the host.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_UNANSWERABLE_CALL_DID_NOT_RUN_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_UNANSWERABLE_CALL_DID_NOT_RUN_VAR_1
-->
${TOOL_RESULT_REMOTE_TOOL_UNANSWERABLE_CALL_DID_NOT_RUN_VAR_0.message} The call did not run on ${TOOL_RESULT_REMOTE_TOOL_UNANSWERABLE_CALL_DID_NOT_RUN_VAR_1.name}.
