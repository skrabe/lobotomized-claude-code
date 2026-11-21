<!--
name: 'App screenshot: stale occluded cont'
description: >-
  Continuation: app stops redrawing while covered, with action-refused or
  ask-user arm.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_0
  - TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_1
  - TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_2
-->
windows and this app stops redrawing while covered, so the picture shows the last thing it drew. ${TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_0(TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_1,TOOL_RESULT_APP_SCREENSHOT_STALE_OCCLUDED_CONT_VAR_2)?"Actions on this window are refused while it is flagged like this: ask the user to leave part of the window visible, then app_screenshot again.":"Ask the user to leave part of the window visible, or act and then app_screenshot again to confirm."}

