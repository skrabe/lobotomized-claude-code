<!--
name: 'Tool Result: mid-delivery key focus elsewhere'
description: >-
  Mid-delivery refusal: key focus moved; remaining input not delivered; refocus,
  screenshot, retry.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_0
  - TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_1
  - TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_2
  - TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_3
  - TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_4
-->
${TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_0}: ${TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_1(TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_2.owner)} while "${TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_3(TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_4)}" is frontmost. Keystrokes go to the app holding keyboard focus, so the remaining input was NOT delivered. Left-click inside "${TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_3(TOOL_RESULT_COMPUTER_USE_RECHECK_KEY_FOCUS_ELSEWHERE_VAR_4)}" to give it keyboard focus (or ask the user to dismiss the panel), take a screenshot to see what was actually typed, then retry.
