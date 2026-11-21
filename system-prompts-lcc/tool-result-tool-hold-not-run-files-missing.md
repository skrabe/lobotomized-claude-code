<!--
name: 'Tool Result: Tool hold not run files missing'
description: >-
  Tells Claude a held tool call was not run because session files may be missing
  or stale and how to proceed
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_0
  - TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_1
  - TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_2
-->
Not run: ${TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_0}, so files can be missing or old. ${TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_1===TOOL_RESULT_TOOL_HOLD_NOT_RUN_FILES_MISSING_VAR_2?"Send the command again to run it anyway.":"A file that looks missing may exist, and your next call will run on what is here. If you were told how to fetch the files, do that first. Otherwise say in your answer that files may be missing or old."}
