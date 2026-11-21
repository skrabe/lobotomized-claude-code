<!--
name: 'Tool result: focus only, caret not placed'
description: >-
  App-action error when the field got focus but the caret could not be placed
  and confirmed; explains how to move it with app_key or retry on a character.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_0
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_1
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_2
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_3
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_4
  - TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_5
-->
Focus only: ${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_0}${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_1}${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_2} now holds keyboard focus, but the caret could NOT be placed at ${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_3} and confirmed (${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_4}). It is wherever the field has it now: look at a fresh app_screenshot. From there app_key (left, right, home, end) moves it${TOOL_RESULT_COMPUTER_USE_CARET_NOT_PLACED_FOCUS_ONLY_VAR_5?"":' and app_type with target: "focused" types at it'}. Or try a point right on a character of the text.
