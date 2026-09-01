<!--
name: 'System Reminder: Brief mode user-facing output'
description: >-
  Reminds Claude that plain assistant text is hidden in brief mode and
  user-facing output must be sent through SendUserMessage
ccVersion: 2.1.178
variables:
  - SEND_USER_MESSAGE_TOOL_NAME
-->

Your substantive reply has not reached the user. Call ${SEND_USER_MESSAGE_TOOL_NAME} now with that reply, addressing only what the user asked; don't mention this reminder. If you have nothing useful to tell the user, end the turn without calling it.
