<!--
name: 'System Reminder: MCP App views shared state by widget_id'
description: >-
  Reminder listing MCP App views with shared state by widget_id and how to read
  one or all
ccVersion: 2.1.319
variables:
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_0
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_2
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_3
-->
MCP App views with shared state, by widget_id: ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_0.join(", ")+(SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1>0?`, and ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1} more`:"")}. ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_2} To read one, call ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_3} with its widget_id; with no arguments it returns every held view.
