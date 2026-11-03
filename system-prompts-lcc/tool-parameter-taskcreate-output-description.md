<!--
name: 'Tool Parameter: TaskCreate output description'
description: >-
  Output schema field: the task's description as saved, which can differ from
  the input after correction or a PreToolUse hook
ccVersion: 2.1.317
-->
The task's description as saved. It can differ from the tool_use input if Claude Code corrects a malformed call or a PreToolUse hook changes the input. Absent in results from older Claude Code versions.
