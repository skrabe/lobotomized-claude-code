<!--
name: 'Slash Command: /plan — cloud session did not confirm the mode switch'
description: >-
  Tells the model the user's plan description was dropped en route to the cloud
  session and instructs how to recover it, so the model does not act as if it
  received the description.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_TIMEOUT_VAR_0
-->
Enabled plan mode locally, but the cloud session didn’t confirm the switch in time — your description was not sent: ${SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_TIMEOUT_VAR_0}. The session may be having connection trouble; once it’s responding again, send the description as a normal message.
