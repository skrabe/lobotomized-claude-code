<!--
name: 'Slash Command: /effort ultracode unavailable'
description: >-
  Tells Claude that ultracode isn't available on the current model/host and
  lists the valid effort options, as the message returned by the /effort
  ultracode command handler.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_EFFORT_ULTRACODE_UNAVAILABLE_VAR_0
  - SLASH_COMMAND_EFFORT_ULTRACODE_UNAVAILABLE_VAR_1
-->
Ultracode isn't available on ${SLASH_COMMAND_EFFORT_ULTRACODE_UNAVAILABLE_VAR_0}. Options: ${SLASH_COMMAND_EFFORT_ULTRACODE_UNAVAILABLE_VAR_1(SLASH_COMMAND_EFFORT_ULTRACODE_UNAVAILABLE_VAR_0)}
