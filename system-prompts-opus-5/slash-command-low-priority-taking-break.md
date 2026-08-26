<!--
name: 'Slash Command: /low-priority Taking a Break'
description: >-
  /low-priority stdout when lower-priority mode is in cooloff after waiting too
  long for spare capacity.
ccVersion: 2.1.246
variables:
  - SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_0
  - SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_1
  - SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_2
  - SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_3
-->
Lower-priority mode is taking a break until ${SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_0(SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_1.ceil(SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_2/1000))??"later"}, after waiting too long for spare capacity. Try /${SLASH_COMMAND_LOW_PRIORITY_TAKING_BREAK_VAR_3} again then.
