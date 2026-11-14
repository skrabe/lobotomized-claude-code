<!--
name: 'Slash Command: /permissions — rule added'
description: >-
  /permissions result line reporting an added allow/deny/ask rule, noting when
  it applies to this session only
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_0
  - SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_1
  - SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_2
  - SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_3
-->
Added ${SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_0.ruleBehavior} rule ${SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_1.bold(SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_2(SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_3(SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_0.ruleValue)))}${SLASH_COMMAND_PERMISSIONS_RULE_ADDED_VAR_0.source==="session"?" for this session only, not saved to settings":""}
