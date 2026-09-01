<!--
name: 'System Reminder: Memory extraction turn budget'
description: >-
  Instructs the memory extraction subagent to batch memory reads before issuing
  memory edits and writes
ccVersion: 2.1.178
variables:
  - EDIT_TOOL_NAME
  - READ_TOOL_NAME
  - WRITE_TOOL_NAME
-->
Limited turn budget. ${EDIT_TOOL_NAME} requires a prior ${READ_TOOL_NAME} of the same file, so: turn 1 — all ${READ_TOOL_NAME} calls in parallel for every file you might update; turn 2 — all ${WRITE_TOOL_NAME}/${EDIT_TOOL_NAME} calls in parallel. Don't interleave reads and writes across turns.
