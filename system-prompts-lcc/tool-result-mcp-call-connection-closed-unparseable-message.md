<!--
name: 'Tool Result: MCP call connection closed on unparseable message'
description: >-
  Error returned to an mcp_call when the MCP server sent a message too large or
  unparseable and Claude Code closed the connection: no result, the server may
  have run the tool, check effect before retrying.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_MCP_CALL_CONNECTION_CLOSED_UNPARSEABLE_MESSAGE_VAR_0
-->
MCP server ${TOOL_RESULT_MCP_CALL_CONNECTION_CLOSED_UNPARSEABLE_MESSAGE_VAR_0} sent a message that was too large or could not be parsed, so Claude Code closed the connection and this mcp_call got no result. The server may have run the tool, so check whether the call took effect before retrying mcp_call.
