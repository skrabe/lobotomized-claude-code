<!--
name: Upload unavailable for request
description: >-
  Says the upload service refused for an unrecognized reason; do not retry, tell
  the user.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NOT_AVAILABLE_FOR_REQUEST_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NOT_AVAILABLE_FOR_REQUEST_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NOT_AVAILABLE_FOR_REQUEST_VAR_0} was not sent: Claude's upload service said that sending files to connectors is not available for this request, for a reason this version of Claude Code does not recognize. Do not retry. Tell the user; a newer version of Claude Code may be able to say why. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_NOT_AVAILABLE_FOR_REQUEST_VAR_1}
