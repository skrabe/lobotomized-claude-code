<!--
name: 'Tool result: MCP task backgrounded exit-only note'
description: >-
  Tells the model, only if the user asks about exiting, that a remote task keeps
  running and checking resumes with the session
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_EXIT_ONLY_NOTE_VAR_0
-->
 Only if the user asks about exiting Claude Code: the task keeps running on the server; checking stops when this session ends, and starts again if they resume the session that started it (${TOOL_RESULT_MCP_TASK_BACKGROUNDED_EXIT_ONLY_NOTE_VAR_0()}) from this folder. If this conversation has since moved to a background session and the task moved with it, that session checks on the task instead.
