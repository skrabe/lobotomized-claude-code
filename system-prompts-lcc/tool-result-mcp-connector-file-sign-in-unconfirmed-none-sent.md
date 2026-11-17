<!--
name: 'Tool Result: Connector sign-in changed, no files sent'
description: >-
  Tail appended to a connector upload refusal when the sign-in changed or could
  not be confirmed and none of the call's files had been sent; asks to check
  with the user again.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_NONE_SENT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_NONE_SENT_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_NONE_SENT_VAR_0===1?"":` None of ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_NONE_SENT_VAR_1} had been sent to the connector.`} Ask the user again before sending.
