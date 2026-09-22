<!--
name: 'Tool Result: App Stale Window Id'
description: >-
  Error tool_result when the given window_id no longer belongs to the granted
  app.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_0
  - TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_1
  - TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_2
-->
window_id ${TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_0} no longer belongs to ${TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_1(TOOL_RESULT_APP_STALE_WINDOW_ID_VAR_2)}. Call app_list_windows again for a fresh id.
