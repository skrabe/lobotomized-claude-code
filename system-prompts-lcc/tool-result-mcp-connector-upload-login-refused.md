<!--
name: Upload sign-in refused
description: >-
  Says the upload service did not accept the sign-in and the user should sign in
  again with /login.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LOGIN_REFUSED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LOGIN_REFUSED_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LOGIN_REFUSED_VAR_0} was not sent: Claude's upload service did not accept this sign-in. Tell the user to sign in again with /login. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LOGIN_REFUSED_VAR_1}
