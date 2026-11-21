<!--
name: 'App screenshot: window not listed by accessibility'
description: 'Capture failure: window on screen but absent from accessibility list.'
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SCREENSHOT_WINDOW_NOT_LISTED_BY_ACCESSIBILITY_VAR_0
-->
The window server shows a window of ${TOOL_RESULT_APP_SCREENSHOT_WINDOW_NOT_LISTED_BY_ACCESSIBILITY_VAR_0} on screen, but accessibility does not list it, so the app_* tools cannot capture it. Take app_screenshot again in a moment; if this stays so, tell the user that this window cannot be captured.
