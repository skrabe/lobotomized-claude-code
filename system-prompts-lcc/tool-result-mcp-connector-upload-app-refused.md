<!--
name: 'Tool result: MCP connector upload refused by desktop app'
description: >-
  Error returned when the Claude desktop app did not send a file to a connector;
  tells Claude not to retry and to tell the user.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_APP_REFUSED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_APP_REFUSED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_APP_REFUSED_VAR_0} was not sent: the Claude desktop app did not send it. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_APP_REFUSED_VAR_1}
