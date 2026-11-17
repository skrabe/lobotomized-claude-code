<!--
name: 'Tool Result: Connector sign-in changed after all files sent'
description: >-
  Tail appended when every file of the call had already been sent to the
  connector before the sign-in was found changed; tells the model to inform the
  user before sending again.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_2
-->
 ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_0===1?"This call's file":`All of ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_1}`} ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_UNCONFIRMED_ALL_SENT_VAR_2} Tell the user before sending again.
