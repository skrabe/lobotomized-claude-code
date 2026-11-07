<!--
name: Connector upload deadline passed
description: >-
  Says the connector's upload deadline passed and to ask the user before a new
  call.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TARGET_EXPIRED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TARGET_EXPIRED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TARGET_EXPIRED_VAR_0} was not sent: the connector's upload deadline passed before the upload started. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_TARGET_EXPIRED_VAR_1} Don't retry on your own. Tell the user the file wasn't sent, and ask before trying again. A new call starts a new upload with a new deadline and may work.
