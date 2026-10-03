<!--
name: 'Tool Result: remote tool background task output file completion line'
description: >-
  Part of the remote background-task note explaining that the task is over if
  its output file ends with an exit/stopped line, and that command output can
  fake that line.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_2
-->
It is over if its output file there (${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_0} with ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_1}: "${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_OUTPUT_FILE_COMPLETION_LINE_VAR_2}") ends with a line saying how it ended, [exited with code N] or [stopped <who or what stopped it>], and nothing the command ran or echoed could have printed that line itself: the command's own output goes to the same file and can say the same words.
