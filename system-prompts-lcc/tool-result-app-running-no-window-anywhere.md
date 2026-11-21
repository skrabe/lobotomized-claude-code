<!--
name: App running with no window anywhere
description: 'state_conflict: app shows no window on any desktop; open one with app_menu.'
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_RUNNING_NO_WINDOW_ANYWHERE_VAR_0
-->
${TOOL_RESULT_APP_RUNNING_NO_WINDOW_ANYWHERE_VAR_0} is running, but it shows no window on any desktop. Open one with app_menu (for example File > New, or the window's name in the Window menu), then take app_screenshot. A window that app_list_windows still names for ${TOOL_RESULT_APP_RUNNING_NO_WINDOW_ANYWHERE_VAR_0} is not on screen, and acting on it reaches nothing. If app_menu brings none either, tell the user that ${TOOL_RESULT_APP_RUNNING_NO_WINDOW_ANYWHERE_VAR_0} shows no window.
