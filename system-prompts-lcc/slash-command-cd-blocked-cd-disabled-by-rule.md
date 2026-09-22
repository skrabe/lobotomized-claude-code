<!--
name: 'Slash Command: /cd — /cd disabled by a permission rule'
description: >-
  Tells the model directory changes are switched off by a named permission rule
  in a named settings source and that the rule must be edited in /permissions
  before any move is possible.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_0
  - SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_1
  - SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_2
  - SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_3
-->
Can't move to ${SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_0(SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_1)} — /cd is turned off by the ${SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_0(SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_2)} rule in ${SLASH_COMMAND_CD_BLOCKED_CD_DISABLED_BY_RULE_VAR_3}. Update the rule in /permissions to move between directories again.
