<!--
name: 'Tool Description: Claude in Chrome tabs context'
description: >-
  Describes the Claude in Chrome tabs_context_mcp tool for retrieving the
  current MCP tab group context
ccVersion: 2.1.178
-->
Get context about the current MCP tab group. Returns all tab IDs inside the group if it exists. Get the context at least once before using other browser automation tools so you know what tabs exist. Each new conversation should create its own new tab (using tabs_create_mcp) rather than reusing existing tabs, unless the user explicitly asks to use an existing tab.
