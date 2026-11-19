<!--
name: 'Tool Result: TaskStop stop unconfirmed'
description: >-
  TaskStop result when the remote machine did not confirm the stop, so the task
  may still be running
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_TASKSTOP_STOP_UNCONFIRMED_VAR_0
  - TOOL_RESULT_TASKSTOP_STOP_UNCONFIRMED_VAR_1
-->
Task ${TOOL_RESULT_TASKSTOP_STOP_UNCONFIRMED_VAR_0.taskId} may still be running: the machine that runs it did not confirm the stop. Another ${TOOL_RESULT_TASKSTOP_STOP_UNCONFIRMED_VAR_1} cannot reach it, and no notice will come when it ends.
