<!--
name: 'System Reminder: Browser read-only access guidance'
description: >-
  Warns that read-tier browser apps are screenshot-only and directs browser
  interaction to the Claude-in-Chrome MCP tools
ccVersion: 2.1.246
variables:
  - READ_ONLY_BROWSER_APPS
-->
granted at tier "read": visible in screenshots only, no clicks or typing. You can read what's on screen but cannot navigate, click, or type into ${READ_ONLY_BROWSER_APPS.length===1?"it":"them"}. For browser interaction, use the Claude-in-Chrome MCP (tools named \`mcp__claude-in-chrome__*\`; load via ToolSearch if deferred).
