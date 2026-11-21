<!--
name: 'Tool result: MCP resource directory server not connected'
description: >-
  Directory-listing tool error: the server is not connected yet; call the
  resource lister for it first, then retry.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_SERVER_NOT_CONNECTED_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_SERVER_NOT_CONNECTED_VAR_1
-->
Server "${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_SERVER_NOT_CONNECTED_VAR_0.name}" is not connected yet, so this tool cannot tell if it supports directory listing. First call ${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_SERVER_NOT_CONNECTED_VAR_1} with "server" set to "${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_SERVER_NOT_CONNECTED_VAR_0.name}". Then call this tool again.
