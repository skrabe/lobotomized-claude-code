<!--
name: 'Tool Result: poll nothing reported background tasks running'
description: >-
  Poll/yield tool result when the wait limit passed with nothing reported while
  background tasks still run, telling the model to call again to keep waiting.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_0
  - TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_1
  - TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_2
-->
nothing has reported yet; ${TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_0.length} background ${TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_1(TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_0.length,"task")} still running. Call ${TOOL_RESULT_POLL_NOTHING_REPORTED_BACKGROUND_TASKS_RUNNING_VAR_2} again to keep waiting.
