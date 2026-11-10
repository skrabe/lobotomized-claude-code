<!--
name: 'Tool Result: Start task attach name not plain'
description: >-
  Refusal to attach a file whose name has a backslash, control or text-direction
  character, asking to copy or rename it
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_0
  - TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_1
  - TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_2
-->
Cannot attach ${TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_0(TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_1)}: a file handed to a task from this session's cloud environment needs a plain name, without a backslash, a line break, another control character or a character that changes text direction. Copy or rename it and attach that. ${TOOL_RESULT_START_TASK_ATTACH_NAME_NOT_PLAIN_VAR_2.words.nothingDone}
