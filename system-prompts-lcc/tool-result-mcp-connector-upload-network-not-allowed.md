<!--
name: 'Tool result: MCP connector upload network not allowed'
description: >-
  Connector file-upload error when the organization only allows Claude access
  from certain networks.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NETWORK_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NETWORK_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NETWORK_NOT_ALLOWED_VAR_0} was not sent: the organization allows access to Claude only from certain networks, and this request didn't come from one of them. Do not retry until the user has connected from an allowed network. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NETWORK_NOT_ALLOWED_VAR_1}
