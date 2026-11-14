<!--
name: Connector not verified
description: >-
  Says the upload service could not confirm the connector is set up as
  Anthropic's connector directory lists it; do not retry, tell the user, and
  note what removing and re-adding it resets.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_0} was not sent: Claude's upload service could not confirm that this connector is set up as Anthropic's connector directory lists it, at a listed address and with a listed way of signing in. Do not retry. Tell the user; whoever manages this organization's connectors can check it. Removing it and adding it again from the directory may fix this, but removing it can reset who may use it, withdraw health-data consents given for it and remove extra accounts people added to it. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_CONNECTOR_NOT_VERIFIED_VAR_1}
