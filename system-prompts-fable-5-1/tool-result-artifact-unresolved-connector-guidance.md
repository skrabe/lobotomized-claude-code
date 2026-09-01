<!--
name: Artifact Unresolved Connector Guidance
description: >-
  Model-facing tool_result fragment telling the model how to set the `server`
  segment for an unresolved MCP connector when an artifact's MCP manifest is
  rejected.
ccVersion: 2.1.246
-->
set `server` to the segment between `mcp__` and the next `__` of a tool name from this session (for `mcp__claude_ai_Slack_beta__search`, use `claude_ai_Slack_beta`, copied exactly), or to the connector's exact display name
