<!--
name: 'Tool Result: Served tool start directory gone'
description: >-
  Rejection telling the model a served tool call was not run because its
  starting directory is gone, and that the next shell command will name the new
  start directory.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_VAR_0
  - TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_VAR_1
-->
${TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_VAR_0} was not run: the directory it was to start in is gone (deleted, moved, replaced by a link, or unreadable). Your next shell command will be refused as well, and its answer names the directory that calls start in from then on. Then send this call again. What is gone: ${TOOL_RESULT_SERVED_TOOL_START_DIRECTORY_GONE_VAR_1}
