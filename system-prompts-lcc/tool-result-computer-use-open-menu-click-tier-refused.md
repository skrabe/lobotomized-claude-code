<!--
name: 'Tool result: computer use open menu at click tier refused'
description: Refusal for clicking an open menu of an app granted only at tier click.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_1
  - TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_2
-->
Refused: ${TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_0==="cursor"?"the mouse cursor":"that point"} is on an open menu of "${TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_1(TOOL_RESULT_COMPUTER_USE_OPEN_MENU_CLICK_TIER_REFUSED_VAR_2)}", which is granted at tier "click". A menu item acts like a keyboard shortcut, so it needs tier "full". At tier "click", plain left_click still works outside the menu: left_click an empty spot in the app's window to close it. For anything on the menu, ask the user to do it themselves.
