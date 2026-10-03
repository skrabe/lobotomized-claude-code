<!--
name: 'Tool Result: remote tool background task on host with task ID'
description: >-
  Remote Bash result note that the command keeps running as a background task on
  the machine, with check/stop instructions and a warning not to use
  pgrep/pkill/kill under the sandbox.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_3
-->
(that command keeps running as a background task ON ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_0}: its ID and output file exist there, not here, and this session is not notified when it finishes. ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_1} To stop it, call ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_2} with that ID and ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_3}: "${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_TASK_ON_HOST_WITH_TASK_ID_VAR_0}". Never check on it or stop it with pgrep, pkill or kill: with the sandbox on there, a later command cannot see or reach this process, or a server it started. To test such a server, do it inside the same command, or ask the user to turn the sandbox off for that folder.)
