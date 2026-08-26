<!--
name: 'Tool Hosts Notice: Header When No Primary Host'
description: >-
  Header when remotes exist but none serve Bash: host MCP tools run there when
  called directly; everything else runs here.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_MCP_PASSTHROUGH_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_HEADER_MCP_PASSTHROUGH_VAR_1
-->
Machines attached to this session — their own MCP tools (mcp__${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_MCP_PASSTHROUGH_VAR_0}__…) run there when called directly; everything else runs here (${SYSTEM_REMINDER_TOOL_HOSTS_HEADER_MCP_PASSTHROUGH_VAR_1()}, the default):
