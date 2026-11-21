<!--
name: 'Tool Result: key focus held elsewhere at gate'
description: >-
  Refusal: another app holds keyboard focus while target is frontmost;
  left-click to focus and retry.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_0
  - TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_1
  - TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_2
  - TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_3
-->
${TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_0(TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_1.owner)} while "${TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_2(TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_3)}" is frontmost. Keystrokes go to the app holding keyboard focus, not the frontmost app, so the input was not delivered. Left-click inside "${TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_2(TOOL_RESULT_COMPUTER_USE_GATE_KEY_FOCUS_ELSEWHERE_VAR_3)}" to give it keyboard focus (or ask the user to dismiss the panel), take a screenshot, then retry.
