<!--
name: 'Tool Result: MCP connector file approval already used'
description: Refuses a second send under an already-used approval as a Claude Code bug
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_APPROVAL_ALREADY_USED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_APPROVAL_ALREADY_USED_VAR_1
-->
No file was sent a second time: the approval this call was given has already been used for one send, and every send takes an approval of its own. This is a bug in Claude Code; the user cannot fix it. ${TOOL_RESULT_MCP_CONNECTOR_FILE_APPROVAL_ALREADY_USED_VAR_0(TOOL_RESULT_MCP_CONNECTOR_FILE_APPROVAL_ALREADY_USED_VAR_1.name)} was not called again.
