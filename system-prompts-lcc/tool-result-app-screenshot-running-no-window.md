<!--
name: 'App screenshot: running but no window'
description: >-
  Capture failure: app running with no window found; open_application or
  app_menu to open one.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SCREENSHOT_RUNNING_NO_WINDOW_VAR_0
-->
${TOOL_RESULT_APP_SCREENSHOT_RUNNING_NO_WINDOW_VAR_0} is running, but no window of it could be found, and none appeared while this call waited for one. Call open_application, which asks a running app to open a window again. If there is still none, open one with app_menu (for example File > New, or the window's name in the Window menu), then take app_screenshot again.
