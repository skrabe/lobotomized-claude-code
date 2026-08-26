<!--
name: 'Tool Result: Remote Host Restarted Command Lost'
description: >-
  host_restarted tool_result when Claude Code on the machine restarted and the
  in-flight command was lost with it.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_0
  - TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_1
  - TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_2
-->
${TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_0(TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_1,TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_2)}, and Claude Code on ${TOOL_RESULT_REMOTE_HOST_RESTARTED_COMMAND_LOST_VAR_1} has restarted since: the command was lost with it. It may have partially run before the restart — check its effect before repeating it.
