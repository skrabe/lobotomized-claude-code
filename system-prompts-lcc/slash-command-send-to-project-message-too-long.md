<!--
name: 'Send to Project: Typed message too long'
description: >-
  /send-to-project command result when the typed message exceeds the byte limit;
  nothing was sent.
ccVersion: 2.1.314
variables:
  - SLASH_COMMAND_SEND_TO_PROJECT_MESSAGE_TOO_LONG_VAR_0
-->
The message is too long to send with /send-to-project, which takes ${SLASH_COMMAND_SEND_TO_PROJECT_MESSAGE_TOO_LONG_VAR_0.toLocaleString("en-US")} bytes. Shorten it and run the command again. Nothing was sent.
