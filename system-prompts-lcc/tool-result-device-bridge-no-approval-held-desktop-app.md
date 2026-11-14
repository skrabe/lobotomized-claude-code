<!--
name: 'Tool Result: Device bridge no approval held (desktop app)'
description: >-
  Tells the model the session service holds no user approval for the call so
  nothing ran, to retry once, and to tell the user if refused the same way
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_NO_APPROVAL_HELD_DESKTOP_APP_VAR_0
-->
The session service holds no approval from the user for this call, so nothing ran on ${TOOL_RESULT_DEVICE_BRIDGE_NO_APPROVAL_HELD_DESKTOP_APP_VAR_0}. The call needs their approval on a card, and this session could not show them one or got no answer. Retry once if the call is still needed. If it is refused the same way, tell the user that the call needs their approval and that this session could not get it.
