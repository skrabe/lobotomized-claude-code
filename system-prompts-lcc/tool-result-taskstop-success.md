<!--
name: 'Tool Result: TaskStop success'
description: >-
  Reports the stopped task and command, with any leftover processes being
  stopped
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0
  - TOOL_RESULT_TASKSTOP_SUCCESS_VAR_1
-->
Successfully stopped task: ${TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0.taskId} (${TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0.command})${TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0.endedLeftovers===void 0?"":`. Also stopping ${TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0.endedLeftovers} ${TOOL_RESULT_TASKSTOP_SUCCESS_VAR_1(TOOL_RESULT_TASKSTOP_SUCCESS_VAR_0.endedLeftovers,"process","processes")} left running by its earlier commands or those of agents it started.`}
