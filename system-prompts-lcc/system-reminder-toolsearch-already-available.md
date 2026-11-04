<!--
name: 'System Reminder: ToolSearch tools already available'
description: >-
  Meta note after a ToolSearch result saying the matched tools are already
  loaded and can be called directly.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_TOOLSEARCH_ALREADY_AVAILABLE_VAR_0
  - SYSTEM_REMINDER_TOOLSEARCH_ALREADY_AVAILABLE_VAR_1
-->
Already available in this conversation: ${SYSTEM_REMINDER_TOOLSEARCH_ALREADY_AVAILABLE_VAR_0(SYSTEM_REMINDER_TOOLSEARCH_ALREADY_AVAILABLE_VAR_1)}. Call ${SYSTEM_REMINDER_TOOLSEARCH_ALREADY_AVAILABLE_VAR_1.length===1?"it":"them"} directly; no search is needed.
