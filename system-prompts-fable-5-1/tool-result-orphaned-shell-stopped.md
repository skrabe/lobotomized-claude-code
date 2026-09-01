<!--
name: Orphaned background shell (stopped) task result
description: >-
  XML-wrapped task-result block delivered to the model on resume reporting a
  stopped background shell command with no completion record.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_0
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_1
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_2
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_3
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_4
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_5
  - TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_6
-->
<${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_0}>
<${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_1}>${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_2(TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_3.taskId)}</${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_1}>
<${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_4}>${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_2(TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_3.toolUseId)}</${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_4}>
<${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_5}>stopped</${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_5}>
<${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_6}>${"No completion record was found for this background shell command from the previous session. It may have been stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. Check the output file for partial results before assuming it completed."}</${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_6}>
</${TOOL_RESULT_ORPHANED_SHELL_STOPPED_VAR_0}>
