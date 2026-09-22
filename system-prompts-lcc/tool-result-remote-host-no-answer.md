<!--
name: 'Tool Result: Remote Host No Answer'
description: >-
  Error tool-result when a remote-host permission prompt times out without
  approval, telling the model nothing ran.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_1
  - TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_2
-->
No one approved or denied this within ${TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_0.round(TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_1/1000)} s, so it was not run on ${TOOL_RESULT_REMOTE_HOST_NO_ANSWER_VAR_2}. Nothing changed there. Continue with work that doesn't need this command and tell the user what you skipped; if it is essential, ask them directly.
