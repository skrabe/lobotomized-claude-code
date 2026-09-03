<!--
name: 'System Reminder: Project memory disconnected'
description: >-
  Warns that a prior shared project-memory connection and its results are stale
  after disconnect or failed reconnection, and directs the agent to re-check
  with memory_list
ccVersion: 2.1.227
variables:
  - FORMAT_MEMORY_PROJECT_FN
  - PREVIOUS_MEMORY_CONNECTION_STATE
  - MEMORY_CONNECTION_OUTCOME
  - IS_PROJECT_SELECTION_DROPPED
  - MEMORY_TOOL_NAMES
  - MEMORY_LIST_TOOL_NAME
-->
This session is no longer connected to ${FORMAT_MEMORY_PROJECT_FN(PREVIOUS_MEMORY_CONNECTION_STATE.project)} (${MEMORY_CONNECTION_OUTCOME==="disconnected"?"the user turned it off in /memory":IS_PROJECT_SELECTION_DROPPED?"the project the user re-picked is no longer available, so the pick was cleared and nothing connected":"reconnecting to the re-picked project failed"}). Any connected memory store list or shared memory index your system prompt may carry, and any ${MEMORY_TOOL_NAMES} results earlier in this conversation, are stale, and nothing is connected for the memory tools to serve until the user reconnects in /memory (${MEMORY_LIST_TOOL_NAME} with no arguments reports what, if anything, is connected whenever you need to re-check). If the user asks you to remember something, use your personal memory directory if your system prompt names one; otherwise explain that project memory is disconnected for this session.
