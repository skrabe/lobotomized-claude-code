<!--
name: 'Tool Result: Remote Host Reconnect Hold Gave Up'
description: >-
  Suffix on a remote-machine tool error telling Claude the call already waited
  for the machine to reconnect and gave up, and to use it again if the session
  is later told it is back.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_0
  - TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_1
  - TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_2
-->
This call already waited up to ${TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_0.round(TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_1/1000)} s for ${TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_2} to come back; if this session is later told that ${TOOL_RESULT_REMOTE_HOST_RECONNECT_HOLD_GAVE_UP_VAR_2} is back, use it again from then.
