<!--
name: 'Tool Result: device bridge host unreachable'
description: >-
  Tool result telling the model a linked computer is not answering because
  Claude there is not connected, so the call did not run; retry shortly or ask
  the user to check that Claude is running on it.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_VAR_0
-->
${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_VAR_0} is not answering right now — most often because Claude on it is not connected (the computer may be offline or asleep, or reconnecting after another session used it); the call did not run. Try again shortly, or ask the user to check that Claude is running on ${TOOL_RESULT_DEVICE_BRIDGE_HOST_UNREACHABLE_VAR_0}.
