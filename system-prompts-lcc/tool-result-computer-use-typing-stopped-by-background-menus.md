<!--
name: 'Tool result: typing stopped by background pop-up menus'
description: >-
  App-type error when typing was halted because keystrokes kept opening a native
  dropdown; tells the model not to retype and to app_click the field first.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_0
  - TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_1
  - TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_2
-->
Typing was stopped after the first ${TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_0.deliveredPrefixChars??"few"} characters were sent, because keys of this text kept opening a native pop-up menu (a dropdown) in ${TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_1(TOOL_RESULT_COMPUTER_USE_TYPING_STOPPED_BY_BACKGROUND_MENUS_VAR_2)}. So the keyboard focus is on a dropdown and not in a text field. Some of those characters may have been lost or have changed its value. Take a fresh app_screenshot, and do NOT type the rest, or the whole string, into the same place: app_click the text field first.
