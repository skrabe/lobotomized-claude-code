<!--
name: Claude Code upload fault
description: >-
  Says Claude Code stopped before sending because of its own code or
  configuration fault.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLIENT_FAULT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLIENT_FAULT_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLIENT_FAULT_VAR_0} was not sent: Claude Code stopped before sending it because of a fault on its own side, in its code or its configuration, not because of the connector or the user's sign-in. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CLIENT_FAULT_VAR_1}
