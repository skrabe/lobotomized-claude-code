<!--
name: 'Slash Command: /color retry hint'
description: >-
  Appends a hint to run /color again after a timeout, failed request or HTTP
  429/5xx when saving the color to the cloud session
ccVersion: 2.1.319
variables:
  - SLASH_COMMAND_COLOR_RETRY_HINT_VAR_0
  - SLASH_COMMAND_COLOR_RETRY_HINT_VAR_1
-->
${SLASH_COMMAND_COLOR_RETRY_HINT_VAR_0} Run /color ${SLASH_COMMAND_COLOR_RETRY_HINT_VAR_1} to try again.
