<!--
name: 'Tool result: ReadMcpResource CCR meta server withheld from subagent'
description: >-
  Thrown when a subagent or background session tries to read resources of the
  CCR meta server.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_READ_MCP_RESOURCE_CCR_META_SUBAGENT_WITHHELD_VAR_0
-->
Claude Code doesn't read resources of server "${TOOL_RESULT_READ_MCP_RESOURCE_CCR_META_SUBAGENT_WITHHELD_VAR_0.name}" from a subagent or a background session, because the server would read the request as the main session's. Use its tools if you have them.
