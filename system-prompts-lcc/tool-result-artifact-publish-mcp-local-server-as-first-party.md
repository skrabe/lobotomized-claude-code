<!--
name: Artifact Publish Mcp Local Server As First Party
description: >-
  Tool result when capabilities.mcp would bind the Claude app's built-in server
  while a same-named local MCP server exists.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_2
-->
"${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_1.server,{max:70})}" would bind the Claude app's own built-in server, but this session also has an MCP server named "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_2}" — the page may have been built against that server, which no viewer can reach; rename or remove "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_SERVER_AS_FIRST_PARTY_VAR_2}" (or drop the declaration) and publish again
