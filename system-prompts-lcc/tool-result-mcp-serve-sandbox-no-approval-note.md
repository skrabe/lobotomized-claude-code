<!--
name: 'Tool Result: MCP serve sandboxed command note'
description: >-
  Note appended to a failed sandboxed command result in claude mcp serve: it
  cannot ask for approval, ignores dangerouslyDisableSandbox and
  excludedCommands, and the user can change settings.
ccVersion: 2.1.326
-->
[serve-mode] This command ran in the sandbox. claude mcp serve cannot ask for approval, so it ignores dangerouslyDisableSandbox and sandbox.excludedCommands. If the sandbox blocked the command, tell the user: they can change the sandbox settings or run it themselves.
