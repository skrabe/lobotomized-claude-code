<!--
name: 'Tool Result: turn-end button label lone sign'
description: >-
  Label check reason: a sign stands on its own where it may only end the label
  or stand between two words
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_0
  - TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_1
  - TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_2
-->
has ${TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_0(TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_1)} on its own, which may only ${TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_2.has(TOOL_RESULT_TURN_END_BUTTON_LABEL_LONE_SIGN_VAR_1)?"end the label, right after a word":"stand between two words"}
