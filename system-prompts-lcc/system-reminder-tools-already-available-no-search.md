<!--
name: 'System Reminder: Tools already available, no search'
description: >-
  ToolSearch meta note listing matched tools already in the conversation and
  telling the model to call them directly without searching.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_0
  - SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_1
  - SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_2
-->
Already available in this conversation: ${SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_0(SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_1)}. ${SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_2(SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_1,`Call ${SYSTEM_REMINDER_TOOLS_ALREADY_AVAILABLE_NO_SEARCH_VAR_1.length===1?"it":"them"} directly; no search is needed.`)}
