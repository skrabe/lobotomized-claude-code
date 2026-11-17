<!--
name: 'Raw connector call refused: path object held'
description: >-
  Refusal when a raw connector call would pass an object with local_file_path
  straight to the connector.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_2
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_3
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_0} was not called: its argument ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_1(TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_2)} holds an object with a local_file_path, and this call would have passed it straight to the connector, with no file sent.${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_PATH_OBJECT_HELD_VAR_3?"":" Write there another value the tool takes in that argument, or leave it out."}
