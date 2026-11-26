<!--
name: 'Tool result: MCP task not backgrounded (open-task limit)'
description: >-
  Suffix appended to the MCP tool_result when a server-side task could not be
  moved to the background because the conversation's open/starting task limit
  was reached.
ccVersion: 2.1.332
-->


This call offered no background task, because as many tasks are open or starting as this conversation allows. If the tool runs only as a background task, call it again after some of them have ended.
