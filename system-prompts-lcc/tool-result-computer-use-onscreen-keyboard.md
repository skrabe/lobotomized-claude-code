<!--
name: 'Tool Result: on-screen keyboard refusal'
description: 'Refusal: on-screen keyboards are never clicked; use type/key instead.'
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_0
  - TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_1
  - TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_2
-->
${TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_0} "${TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_1({displayName:TOOL_RESULT_COMPUTER_USE_ONSCREEN_KEYBOARD_VAR_2})}", an on-screen keyboard. Its keys type into whichever app has keyboard focus (some keyboards press a key when the pointer merely rests on one), so it is never clicked and the pointer is never placed on it. Use type or key to enter text or press keys; if the keyboard covers what you need, ask the user to move or close it.
