<!--
name: Upload request refused
description: Says the upload service did not accept Claude Code's request; do not retry.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_REQUEST_REFUSED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_REQUEST_REFUSED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_REQUEST_REFUSED_VAR_0} was not sent: Claude's upload service did not accept the request Claude Code made for it. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_REQUEST_REFUSED_VAR_1}
