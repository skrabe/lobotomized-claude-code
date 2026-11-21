<!--
name: 'App screenshot: window_id gone'
description: >-
  Capture failure: requested window_id no longer exists; use app_list_windows or
  omit window_id.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SCREENSHOT_WINDOW_ID_GONE_VAR_0
  - TOOL_RESULT_APP_SCREENSHOT_WINDOW_ID_GONE_VAR_1
-->
window_id ${TOOL_RESULT_APP_SCREENSHOT_WINDOW_ID_GONE_VAR_0} is no longer among ${TOOL_RESULT_APP_SCREENSHOT_WINDOW_ID_GONE_VAR_1}'s windows. Call app_list_windows for the windows it has now, or leave window_id out to capture its main window.
