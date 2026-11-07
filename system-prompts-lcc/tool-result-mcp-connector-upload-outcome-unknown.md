<!--
name: Upload outcome unknown
description: >-
  Says it is unknown whether the file reached the connector; do not resend
  unless the user asks.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_2
-->
It is not known whether ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_0} reached the connector: it may be there. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_1} Tell the user, and do not send ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_OUTCOME_UNKNOWN_VAR_2.length===0?"it":"any of these files"} again unless they ask.
