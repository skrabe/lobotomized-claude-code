<!--
name: /plan cloud mode push timeout
description: >-
  Told the model when plan mode was turned on locally but the cloud session
  didn't confirm, so the description wasn't sent.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_TIMEOUT_VAR_0
-->
Turned on plan mode here, but the cloud session didn’t confirm the switch in time. Your description wasn’t sent: ${SLASH_COMMAND_PLAN_CLOUD_MODE_PUSH_TIMEOUT_VAR_0}. Once the session responds, send it as a normal message.
