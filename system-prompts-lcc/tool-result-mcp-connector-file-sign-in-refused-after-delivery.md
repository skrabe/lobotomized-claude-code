<!--
name: 'Tool Result: MCP connector sign-in refused after files delivered'
description: >-
  Says the call's files were already sent when the connector refused sign-in so
  the tool did not run, and to tell the user before resending
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_3
-->
${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_0.delivered.length<TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_1.connectorFiles.length?`${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_0.delivered.length} of this call's ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_1.connectorFiles.length} files`:TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_1.connectorFiles.length===1?"This call's file":`This call's ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_1.connectorFiles.length} files`} had already been sent to the connector when it refused the sign-in, so ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_2(TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_3.name)} did not ${TOOL_RESULT_MCP_CONNECTOR_FILE_SIGN_IN_REFUSED_AFTER_DELIVERY_VAR_0.again?"finish":"run"}. Tell the user before sending again.
