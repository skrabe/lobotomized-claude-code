<!--
name: 'System Reminder: MCP App views shared state by id'
description: >-
  Lists held MCP App view ids with shared state and how to read one or all of
  them
ccVersion: 2.1.317
variables:
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_0
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_2
  - SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_3
-->
MCP App views with shared state, by view id: ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_0.join(", ")+(SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1>0?`, and ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_1} more`:"")}. ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_2} To read one, call ${SYSTEM_REMINDER_MCP_APP_VIEWS_SHARED_STATE_BY_ID_VAR_3} with its view id; with no arguments it returns every held view.
