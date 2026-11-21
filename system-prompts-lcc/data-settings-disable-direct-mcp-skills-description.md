<!--
name: 'Data: disableDirectMcpSkills setting description'
description: >-
  Description of the `disableDirectMcpSkills` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.330
-->
When true in managed settings, Claude Code lists and loads no skill of an MCP server that it connects to directly, reads no listed file of a loaded one, and lists no directory of the server. On the Team and Enterprise plans these skills are off unless an administrator sets it to false. Connectors that Claude Code reaches through Anthropic keep their skills, and each server keeps its tools. In a user, project or local settings file it has no effect.
