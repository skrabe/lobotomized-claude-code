<!--
name: 'Tool Result: Auto Mode Server Context Stale'
description: >-
  Tells the model a prior auto-mode review is void because the artifact's
  sharing state changed, and to repeat the identical tool call.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_VAR_0
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_VAR_1
-->
This is not a judgement against ${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_VAR_0}. Repeat the identical ${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_VAR_0} call once now; it will be reviewed against the artifact's current state. (${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_VAR_1} reviewed it against this artifact's sharing state as it stood a moment ago — whose artifact it is, who it is shared with, whether its viewers see changes live, or a watch the user stopped — and that state has since changed, so that review no longer applies.) 
