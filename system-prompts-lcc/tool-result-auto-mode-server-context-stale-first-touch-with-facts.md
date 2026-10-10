<!--
name: 'Tool Result: Auto mode stale context first touch with facts'
description: >-
  First-touch variant giving the artifact facts Claude Code looked up for the
  repeated review
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_FIRST_TOUCH_WITH_FACTS_VAR_0
  - TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_FIRST_TOUCH_WITH_FACTS_VAR_1
-->
it will be reviewed with this artifact's facts. (${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_FIRST_TOUCH_WITH_FACTS_VAR_0} reviewed this call before it had been told whose artifact this is or who it is shared with, and a review made that way is not relied on. Claude Code has since looked it up: ${TOOL_RESULT_AUTO_MODE_SERVER_CONTEXT_STALE_FIRST_TOUCH_WITH_FACTS_VAR_1.factsNow}. The repeated call is reviewed with those facts.)
