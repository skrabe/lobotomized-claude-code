<!--
name: 'Tool Result: front app changed after gate'
description: >-
  Refusal: another app became frontmost after gate approval; screenshot before
  retrying.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_2
-->
${TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_0?`"${TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_1(TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_0)}" became frontmost`:"No app is frontmost (focus anomaly)"} after the gate approved "${TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_1(TOOL_RESULT_COMPUTER_USE_GATE_FRONT_APP_CHANGED_VAR_2)}", so the input was not delivered. Take a screenshot to see where focus went before retrying.
