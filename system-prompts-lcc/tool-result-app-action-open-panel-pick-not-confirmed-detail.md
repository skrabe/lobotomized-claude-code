<!--
name: 'Tool result: app action Open panel pick not confirmed'
description: >-
  Result when macOS didn't confirm an Open panel selection: nothing opened,
  re-screenshot before pressing Open.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_0
  - TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_1
  - TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_2
  - TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_3
  - TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_4
-->
macOS did not confirm the selection in this Open panel (${TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_0}${TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_1} at ${TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_2}), so count that item as not picked. Nothing was opened. Take a fresh app_screenshot before the next click, and press the panel's Open button only once it shows a file selected: otherwise Open may act on something else. ${TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_3(TOOL_RESULT_APP_ACTION_OPEN_PANEL_PICK_NOT_CONFIRMED_DETAIL_VAR_4)} Cancel picks no file: it closes the panel and leaves the step undone.
