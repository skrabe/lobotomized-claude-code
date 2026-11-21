<!--
name: 'App zoom: window_id gone'
description: >-
  app_zoom failure: the referenced window is gone; take a fresh screenshot and
  re-pick region.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_ZOOM_WINDOW_ID_GONE_VAR_0
  - TOOL_RESULT_APP_ZOOM_WINDOW_ID_GONE_VAR_1
-->
window_id ${TOOL_RESULT_APP_ZOOM_WINDOW_ID_GONE_VAR_0}, which this zoom refers to, is no longer among ${TOOL_RESULT_APP_ZOOM_WINDOW_ID_GONE_VAR_1}'s windows. Take a fresh app_screenshot and choose the region again.
