<!--
name: 'Tool Description: Check MCP task'
description: >-
  Prompt for the tool that asks an MCP server once for a background task's
  status.
ccVersion: 2.1.331
-->
Asks the MCP server one time for the status of a background MCP task, also of one that was stopped. Use it only when the user asks about the task: how it is going, whether it has finished, or whether a stop worked. Never use it to wait for a task or to poll it: the result comes in a task notification.
