<!--
name: 'Tool Result: Auto mode unavailable turn ended'
description: >-
  Reports that auto mode is unavailable, the call was not run and the turn has
  ended
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_0
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_1
  - TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_2
-->
Auto mode is unavailable: ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_0(TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_1)}, so ${TOOL_RESULT_AUTO_MODE_UNAVAILABLE_TURN_ENDED_VAR_2.name} was not run and this turn has ended. Wait for the user's next message before doing anything further.
