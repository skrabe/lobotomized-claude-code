<!--
name: 'Data: Artifact MCP connector server segment'
description: >-
  Branch of the Artifact MCP connector guidance telling the model to take the
  server value from the mcp__<connector>__<tool> prefix segment, copied exactly,
  resolved to a display name at publish
ccVersion: 2.1.239
-->
Connector tools appear in your tool list as `mcp__<connector>__<toolName>`. Set `server` to the `<connector>` segment — everything between `mcp__` and the next `__` (for `mcp__claude_ai_Slack_beta__search`, the `server` is `claude_ai_Slack_beta`). Copy the segment exactly, case included; when publishing, it is resolved to the connector's display name automatically.
