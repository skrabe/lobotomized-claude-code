<!--
name: 'Tool Result: Connector refused sign-in after asking to repeat'
description: >-
  Note prefixed to the connector's sign-in error when it had asked for the call
  to be made again, so the tool did not finish.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_CALL_AGAIN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_CALL_AGAIN_VAR_1
-->
The connector had asked for the call to be made again when it refused the sign-in, so ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_CALL_AGAIN_VAR_0(TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_CALL_AGAIN_VAR_1.name)} did not finish. Tell the user before calling it again.
