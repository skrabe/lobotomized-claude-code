<!--
name: 'Tool Hosts Notice: Passthrough MCP Tools'
description: >-
  Per-host note that the host's own MCP tools run there with that machine's
  logins; a server this session also runs appears a second time locally.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_PASSTHROUGH_MCP_TOOLS_VAR_0
-->
Its own MCP tools (mcp__${SYSTEM_REMINDER_TOOL_HOSTS_PASSTHROUGH_MCP_TOOLS_VAR_0}__<server>__…) run there when called directly, with the logins saved on that machine; a server this session also runs itself appears a second time as mcp__<server>__…, which runs here.
