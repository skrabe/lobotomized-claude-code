<!--
name: 'Tool Result: Personal hook settings location'
description: >-
  Locates the failing personal hook by index in the user's settings file and
  notes edits usually apply without a new session
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_0
  - TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_1
  - TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_2
-->
this hook is ${TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_0}, counted from 0, in ${TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_1("userSettings")} (${TOOL_RESULT_PERSONAL_HOOK_SETTINGS_LOCATION_VAR_2()??"a change saved there usually takes effect without a new session"}); 
