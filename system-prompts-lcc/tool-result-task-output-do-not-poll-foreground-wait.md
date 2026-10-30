<!--
name: 'Tool Result: TaskOutput do not poll foreground wait'
description: >-
  TaskOutput result for a still-running task telling the model not to call it
  again, that the result is delivered automatically, and to wait with one
  foreground command if needed.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_TASK_OUTPUT_DO_NOT_POLL_FOREGROUND_WAIT_VAR_0
-->
Do not call ${TOOL_RESULT_TASK_OUTPUT_DO_NOT_POLL_FOREGROUND_WAIT_VAR_0} again for this task: if the command finishes while you are still working, its result is delivered to you automatically between your tool calls (usually as a ${TOOL_RESULT_TASK_OUTPUT_DO_NOT_POLL_FOREGROUND_WAIT_VAR_0} result, otherwise as a task notification). If you need that result before you reply and nothing else is left to do, wait with one foreground shell command that blocks until the output file shows what you need; otherwise continue with other work.
