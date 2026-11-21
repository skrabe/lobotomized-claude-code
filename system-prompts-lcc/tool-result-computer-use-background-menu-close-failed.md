<!--
name: 'Tool result: background menu close failed'
description: >-
  Note that a native pop-up menu opened in the background and closing it failed;
  tell the user it is open and how to close it.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_COMPUTER_USE_BACKGROUND_MENU_CLOSE_FAILED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_BACKGROUND_MENU_CLOSE_FAILED_VAR_1
-->
${TOOL_RESULT_COMPUTER_USE_BACKGROUND_MENU_CLOSE_FAILED_VAR_0}, and closing it FAILED: the user may be unable to type until it is gone. Look with app_screenshot. If the menu is still up, tell the user at once that a menu of ${TOOL_RESULT_COMPUTER_USE_BACKGROUND_MENU_CLOSE_FAILED_VAR_1} is open and that a click on it closes it. Do not press the control that opened it again in the background.
