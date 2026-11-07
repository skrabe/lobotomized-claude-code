<!--
name: Sign-in check refused upload
description: >-
  Says Claude's sign-in check refused the request without a reason; do not
  retry.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SIGN_IN_CHECK_REFUSED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SIGN_IN_CHECK_REFUSED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SIGN_IN_CHECK_REFUSED_VAR_0} was not sent: Claude's sign-in check refused the request, so this file did not reach the connector; its answer does not say why. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_SIGN_IN_CHECK_REFUSED_VAR_1}
