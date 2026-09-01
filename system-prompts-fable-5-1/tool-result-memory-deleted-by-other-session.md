<!--
name: Memory Deleted By Other Session Notice
description: >-
  Model-facing memory-sync conflict notice delivered as PostToolUse
  additionalContext after a memory tool call, instructing the model to delete
  the file if the deletion was intended.
ccVersion: 2.1.201
variables:
  - TOOL_RESULT_MEMORY_DELETED_BY_OTHER_SESSION_VAR_0
  - TOOL_RESULT_MEMORY_DELETED_BY_OTHER_SESSION_VAR_1
-->
The memory file ${TOOL_RESULT_MEMORY_DELETED_BY_OTHER_SESSION_VAR_0(TOOL_RESULT_MEMORY_DELETED_BY_OTHER_SESSION_VAR_1.path)} was deleted from shared memory by another session while you had local changes. Your local version has been saved to shared memory as a new copy. If the deletion was intended, delete the file.
