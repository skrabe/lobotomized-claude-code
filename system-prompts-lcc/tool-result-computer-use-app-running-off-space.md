<!--
name: 'Tool Result: Computer Use App Running Off Space'
description: >-
  Tells the model the app is on another Space and how app_* versus display-scope
  tools can reach it.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_0
  - TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_1
  - TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_2
-->
${TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_0(TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_1)} is running on another Space. The app_* tools can app_screenshot it there, and for most apps can click/type into it in the background; if an action refuses because the window is off-Space, ${TOOL_RESULT_COMPUTER_USE_APP_RUNNING_OFF_SPACE_VAR_2}.
