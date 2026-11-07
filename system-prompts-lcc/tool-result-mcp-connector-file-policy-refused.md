<!--
name: 'Tool Result: MCP connector file upload refused by policy'
description: >-
  Refuses sending a file to a connector because policy denies or cannot confirm
  it, telling the model to inform the user and not retry with a file
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_3
  - TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_2
-->
No file was sent: ${TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_0[TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_3]} Tell the user; do not retry with a file. ${TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_1(TOOL_RESULT_MCP_CONNECTOR_FILE_POLICY_REFUSED_VAR_2)} A call that sets no file argument is still sent.
