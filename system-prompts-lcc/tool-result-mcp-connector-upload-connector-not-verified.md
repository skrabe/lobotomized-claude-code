<!--
name: Connector not verified
description: >-
  Says the upload service could not verify the connector came from Anthropic's
  directory; tell the user, do not retry.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_0} was not sent: Claude's upload service could not confirm that this connector was added from Anthropic's connector directory at the address the directory lists for it. Do not retry. Tell the user; removing the connector and adding it again from the directory may fix this, and an admin of their organization may need to do that. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_1}
