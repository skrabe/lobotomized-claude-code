<!--
name: 'System Reminder: MCP output truncation warning'
description: >-
  Warns that MCP tool output exceeded the token limit and advises pagination,
  filtering, or noting incomplete results
ccVersion: 2.1.178
variables:
  - MAX_MCP_OUTPUT_TOKENS_FN
-->


[OUTPUT TRUNCATED - exceeded ${MAX_MCP_OUTPUT_TOKENS_FN()} token limit]

The tool output was truncated. If this MCP server provides pagination or filtering tools, use them to retrieve the portion you need. Otherwise tell the user the output is truncated and results may be incomplete.
