<!--
name: 'Tool Result: MCP connector upload tool policy not allowed'
description: >-
  Upload refusal when org settings or the user's role don't allow sending files
  to the connector's tool, or the upload service couldn't check them.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TOOL_POLICY_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TOOL_POLICY_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TOOL_POLICY_NOT_ALLOWED_VAR_0} was not sent: the organization's settings or the user's role don't allow sending files to this connector's tool, or Claude's upload service couldn't check them. Don't retry now. Tell the user their admin can check the settings, and that if the settings already allow it, trying again later may work. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TOOL_POLICY_NOT_ALLOWED_VAR_1}
