<!--
name: 'Tool Result: Working directory unverifiable, every call refused'
description: >-
  Tells the model every tool call in this directory will be refused so it must
  not retry and should tell the user the fix
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_0
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_1
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_2
-->
${TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_0} Every tool call in this directory will be refused the same way, so don't retry. Tell the user to ${TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_1(TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_EVERY_CALL_REFUSED_VAR_2)}.
