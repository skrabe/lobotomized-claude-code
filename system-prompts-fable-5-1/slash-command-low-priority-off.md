<!--
name: 'Slash Command: /low-priority Turned Off'
description: >-
  /low-priority local-command stdout confirming lower-priority mode is off and
  that new messages wait for the usage limit as usual.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_0
  - SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_1
  - SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_2
  - SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_3
-->
Lower-priority mode is off. New messages wait for your usage limit as usual${SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_0(SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_1)||SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_2(SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_1)?`; run /${SLASH_COMMAND_LOW_PRIORITY_OFF_VAR_3} again to turn it back on`:""}.
