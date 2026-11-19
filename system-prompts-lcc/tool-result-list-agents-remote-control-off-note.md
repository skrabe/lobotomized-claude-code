<!--
name: 'Tool Result: List agents remote control off note'
description: >-
  Notes that sessions are missing because Remote Control is off and how to turn
  it on
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_0
  - TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_1
  - TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_2
-->
[${TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_0} ${TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_1?"may be missing from the list":"are not listed"} because Remote Control is off in this session. The user can turn it on with ${TOOL_RESULT_LIST_AGENTS_REMOTE_CONTROL_OFF_NOTE_VAR_2?"the Remote Control switch in the app":"/remote-control"}; then list again.]
