<!--
name: 'Slash Command: /plan — cloud session refused the mode switch'
description: >-
  Tells the model the cloud session rejected plan mode and the user's
  description was therefore never delivered, so it should not treat the
  description as received.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_REJECTED_VAR_0
-->
The cloud session couldn’t switch to plan mode, so your description was not sent: ${SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_REJECTED_VAR_0}
