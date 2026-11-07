<!--
name: Some connector files already sent
description: >-
  Reports how many of the call's files reached the connector before it stopped
  and asks to tell the user before resending.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_4
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_0} was called, and ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_1.length} of ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_2} (${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_1.map(TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_3).join(", ")}) had already been sent to the connector when it stopped${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SOME_SENT_BEFORE_STOP_VAR_4?"; the connector was told which did not arrive":""}. Tell the user before sending any of them again.
