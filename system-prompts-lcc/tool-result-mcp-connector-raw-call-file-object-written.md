<!--
name: 'Tool Result: MCP connector raw call - file object written'
description: Refusal when an argument holds an id/mimeType/size file object.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_0} was not called: its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_FILE_OBJECT_WRITTEN_VAR_2)} holds an object with an id, a mimeType and a size, which is how a file is written for a connector, and this call is not passed on with such an object. Write there another value the tool takes in that argument, or leave it out.
