<!--
name: 'Tool Result: device bridge host unreachable'
description: >-
  Tool result telling the model a linked computer is not answering because
  Claude there is not connected, so the call did not run; do not call it again
  this turn and tell the user to check that Claude is running on it
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_0
  - TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_1
-->
${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_0} is not answering right now — most often because Claude on it is not connected (the computer may be offline or asleep, or reconnecting after another session used it); the call did not run. Do not call ${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_0} again in this turn: do the rest of the task without ${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_0}, and tell the user what is blocked and to check that Claude is running on ${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_0}. ${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_2_VAR_1["away.ending"]()}
