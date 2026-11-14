<!--
name: 'Tool Result: Remote tool host disconnected by person'
description: >-
  Explains the person at the computer disconnected the session from the folder;
  do the rest without it
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_1
-->
The person at ${TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_0} disconnected this session from the folder it was using there. Nothing on ${TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_0} is down. Do the rest of the task without ${TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_0} and tell the user what that leaves undone; ask for the folder again only if the user wants you to. ${TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_1(TOOL_RESULT_REMOTE_TOOL_HOST_RELEASED_BY_PERSON_VAR_0)}
