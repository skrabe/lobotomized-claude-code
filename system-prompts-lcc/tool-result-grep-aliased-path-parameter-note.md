<!--
name: 'Tool Result: Grep aliased path parameter note'
description: >-
  Note appended to the Grep tool result when the model passed file_path instead
  of path, saying file_path was read as path or ignored
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_GREP_ALIASED_PATH_PARAMETER_NOTE_VAR_0
  - TOOL_RESULT_GREP_ALIASED_PATH_PARAMETER_NOTE_VAR_1
-->
${TOOL_RESULT_GREP_ALIASED_PATH_PARAMETER_NOTE_VAR_0}'s parameter for where to search is named \`path\`. ${TOOL_RESULT_GREP_ALIASED_PATH_PARAMETER_NOTE_VAR_1?"`file_path` was read as `path`.":"`file_path` repeated `path` and was ignored."}
