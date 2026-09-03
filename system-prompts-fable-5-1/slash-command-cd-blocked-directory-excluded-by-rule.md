<!--
name: 'Slash Command: /cd — target directory excluded by a rule'
description: >-
  Tells the model this specific directory is excluded by a named rule and gives
  two ways forward — choose a directory outside the rule, or change the rule —
  so it can retry sensibly instead of repeating the same move.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_0
  - SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_1
  - SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_2
  - SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_3
-->
Can't move to ${SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_0(SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_1)} — it's excluded by the ${SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_0(SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_2)} rule in ${SLASH_COMMAND_CD_BLOCKED_DIRECTORY_EXCLUDED_BY_RULE_VAR_3}. Pick a directory outside that rule, or update it in /permissions.
