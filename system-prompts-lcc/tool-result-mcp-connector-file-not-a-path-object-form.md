<!--
name: 'Tool Result: Connector not-a-path, object form'
description: >-
  Slot describing that each file must be the path form where the shown schema
  has a file object, optionally noting a list of files holds nothing else.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_2
-->
${TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_0}, the path of a file on this computer, where the schema you were shown has that object${TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_1.otherItems||TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_1.nullItems||!TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_1.places.some((TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_2)=>TOOL_RESULT_MCP_CONNECTOR_FILE_NOT_A_PATH_OBJECT_FORM_VAR_2.includes("items"))?"":", and a list of files holds nothing else"}
