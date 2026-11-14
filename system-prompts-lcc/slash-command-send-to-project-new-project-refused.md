<!--
name: 'Slash command: send-to-project new project refused'
description: >-
  Message when a new Claude Project cannot be created for the account, so
  nothing was sent.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_REFUSED_VAR_0
  - SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_REFUSED_VAR_1
-->
A new Claude Project can’t be created for your Claude account (${SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_REFUSED_VAR_0(SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_REFUSED_VAR_1.message)}), so nothing was sent. Run /send-to-project again and pick one of your projects.
