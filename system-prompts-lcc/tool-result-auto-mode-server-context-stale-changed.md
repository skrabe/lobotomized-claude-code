<!--
name: 'Tool Result: Auto mode stale context changed'
description: >-
  Explains the server reviewed the call against artifact sharing state that has
  since changed, with current facts
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_CHANGED_VAR_0
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_CHANGED_VAR_1
-->
it will be reviewed against the artifact's current state. (${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_CHANGED_VAR_0} reviewed it against this artifact's sharing state as it stood a moment ago — whose artifact it is, who it is shared with, whether its viewers see changes live, or a watch the user stopped — and that state, or what Claude Code knows of it, has since changed, so that review no longer applies.${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_CHANGED_VAR_1.factsNow===""?"":` It is now: ${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_CHANGED_VAR_1.factsNow}.`})
