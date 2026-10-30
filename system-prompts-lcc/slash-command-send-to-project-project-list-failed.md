<!--
name: 'Slash command: /send-to-project project list failed'
description: >-
  Tells the model the user's projects could not be listed and to have the user
  retry shortly
ccVersion: 2.1.314
variables:
  - SLASH_COMMAND_SEND_TO_PROJECT_PROJECT_LIST_FAILED_VAR_0
  - SLASH_COMMAND_SEND_TO_PROJECT_PROJECT_LIST_FAILED_VAR_1
-->
Your projects couldn’t be listed just now (${SLASH_COMMAND_SEND_TO_PROJECT_PROJECT_LIST_FAILED_VAR_0(SLASH_COMMAND_SEND_TO_PROJECT_PROJECT_LIST_FAILED_VAR_1.detail)}), so nothing was sent. Tell the user to run /send-to-project again in a moment, and stop.
