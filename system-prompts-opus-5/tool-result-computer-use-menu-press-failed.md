<!--
name: 'Tool Result: app_menu Press Failed'
description: >-
  Error returned when app_menu found a menu item but pressing it failed, likely
  because the item is disabled.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_2
  - TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_3
-->
Menu item ${TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_0.stringify(TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_1)} was found but pressing it failed (${TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_2(TOOL_RESULT_COMPUTER_USE_MENU_PRESS_FAILED_VAR_3.axError)}). It is likely 
