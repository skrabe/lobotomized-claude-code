<!--
name: Connector uploads unavailable with IP allowlist
description: >-
  Says connector file sending is unavailable for organizations using an IP
  allowlist; do not retry from any network.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_IP_ALLOWLIST_NOT_ALLOWED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_IP_ALLOWLIST_NOT_ALLOWED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_IP_ALLOWLIST_NOT_ALLOWED_VAR_0} was not sent: sending files to connectors is not yet available for organizations that allow access only from approved IP addresses, as this one does. Do not retry, from this or another network. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_IP_ALLOWLIST_NOT_ALLOWED_VAR_1}
