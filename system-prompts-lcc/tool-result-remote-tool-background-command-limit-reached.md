<!--
name: 'Tool Result: Remote tool background command limit reached'
description: >-
  Tool result telling Claude a machine already runs the maximum number of
  background commands for this session, that nothing was started, and to wait
  for one to finish or run it in the foreground
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_2
-->
${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_0} already has ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_1} background ${TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_2(TOOL_RESULT_REMOTE_TOOL_BACKGROUND_COMMAND_LIMIT_REACHED_VAR_1,"command")} running or waiting for approval for this session, the most it takes at a time. Nothing was started. Wait for one to finish, or run this one in the foreground.
