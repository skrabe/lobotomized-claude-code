<!--
name: 'Tool Result: Connector files already sent list'
description: >-
  Fragment listing the connector files that had already been sent when the
  sign-in was found changed or unconfirmed.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_SENT_LIST_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_SENT_LIST_VAR_1
-->
(${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_SENT_LIST_VAR_0.map(TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_SENT_LIST_VAR_1).join(", ")}) had already been sent to the connector.
