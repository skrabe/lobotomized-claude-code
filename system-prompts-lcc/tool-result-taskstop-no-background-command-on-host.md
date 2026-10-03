<!--
name: 'Tool Result: TaskStop No Background Command On Host'
description: >-
  TaskStop refusal when no background command with that id is running on the
  named remote host for this session (finished, stopped, or never this
  session's).
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_TASKSTOP_NO_BACKGROUND_COMMAND_ON_HOST_VAR_0
  - TOOL_RESULT_TASKSTOP_NO_BACKGROUND_COMMAND_ON_HOST_VAR_1
-->
No background command with ID ${TOOL_RESULT_TASKSTOP_NO_BACKGROUND_COMMAND_ON_HOST_VAR_0} is running on ${TOOL_RESULT_TASKSTOP_NO_BACKGROUND_COMMAND_ON_HOST_VAR_1.origin.hostName} for this session: it has already finished or been stopped, or it was never this session's.
