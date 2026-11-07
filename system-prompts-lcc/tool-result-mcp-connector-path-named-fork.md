<!--
name: 'Tool Result: MCP connector path through named fork'
description: >-
  Refuses sending a file by a path through a ..namedfork component and asks for
  the file's own path
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_2
-->
Cannot send ${TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_0} ${TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_1}: this path goes through a file's named fork (a part spelled "..namedfork"), and no file is sent to a connector by such a path, wherever it lies. To send that file, give its own path, without the fork. ${TOOL_RESULT_MCP_CONNECTOR_PATH_NAMED_FORK_VAR_2}
