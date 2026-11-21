<!--
name: 'Tool Result: Working directory unverifiable, retry once'
description: >-
  Tells the model to retry the call once and, if refused again, stop and tell
  the user how to fix the working directory
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_0
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_1
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_2
  - TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_3
-->
${TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_0} ${TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_1==="call"?"Make the call again":"Re-issue the command"} once; if it is refused the same way, don't keep retrying: tell the user to ${TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_2(TOOL_RESULT_WORKING_DIRECTORY_UNVERIFIABLE_RETRY_ONCE_VAR_3)}.
