<!--
name: 'Tool result: command start directory recreated'
description: >-
  Error returned when a command was not run because its start directory was gone
  and has been recreated empty.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_COMMAND_START_DIRECTORY_RECREATED_VAR_0
  - TOOL_RESULT_COMMAND_START_DIRECTORY_RECREATED_VAR_1
-->
${TOOL_RESULT_COMMAND_START_DIRECTORY_RECREATED_VAR_0} was not run: the directory it was to start in was gone, and the files in it with it. It has been made again, empty. Check that this call still does what you mean there, then send it again. The directory: ${TOOL_RESULT_COMMAND_START_DIRECTORY_RECREATED_VAR_1}
