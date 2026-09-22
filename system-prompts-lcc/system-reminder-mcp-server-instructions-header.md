<!--
name: MCP Server Instructions Header
description: >-
  Model-facing CC-authored framing/header wrapping per-server MCP instructions
  in the mcp_instructions_delta reminder ("# MCP Server Instructions\n\nThe
  following MCP servers have provided instructions..."); conditional on at least
  one connected MCP server providing instructions.
ccVersion: 2.1.191
variables:
  - SYSTEM_REMINDER_MCP_SERVER_INSTRUCTIONS_HEADER_VAR_0
-->
# MCP Server Instructions

The following MCP servers have provided instructions for how to use their tools and resources:

${SYSTEM_REMINDER_MCP_SERVER_INSTRUCTIONS_HEADER_VAR_0.join(`

`)}
