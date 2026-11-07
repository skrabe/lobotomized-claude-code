<!--
name: Upload service fault
description: Says the upload service failed on Anthropic's side; ask before retrying.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SERVICE_FAULT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SERVICE_FAULT_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SERVICE_FAULT_VAR_0} was not passed on: Claude's upload service failed while handling it, a problem on Anthropic's side. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SERVICE_FAULT_VAR_1} Ask the user before trying again.
