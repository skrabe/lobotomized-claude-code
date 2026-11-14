<!--
name: 'Tool whenToUse: Your computer relay'
description: >-
  Deferred-tool listing line telling Claude not to use the inert 'Your computer'
  tool and to use the matching MCP tool instead.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_YOUR_COMPUTER_RELAY_VAR_0
-->
When a task needs the user's own computer, do not use it, since it does nothing; use the mcp__${TOOL_WHEN_TO_USE_YOUR_COMPUTER_RELAY_VAR_0}__ tool that fits, if you have one.
