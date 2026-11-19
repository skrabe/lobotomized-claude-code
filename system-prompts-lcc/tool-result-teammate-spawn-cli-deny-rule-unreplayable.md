<!--
name: 'Tool result: teammate spawn deny rule unreplayable'
description: >-
  Error saying a deny rule can't be handed to a teammate intact, so the teammate
  was not started, and how to fix it.
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_TEAMMATE_SPAWN_CLI_DENY_RULE_UNREPLAYABLE_VAR_0
  - TOOL_RESULT_TEAMMATE_SPAWN_CLI_DENY_RULE_UNREPLAYABLE_VAR_1
-->
The deny rule "${TOOL_RESULT_TEAMMATE_SPAWN_CLI_DENY_RULE_UNREPLAYABLE_VAR_0(TOOL_RESULT_TEAMMATE_SPAWN_CLI_DENY_RULE_UNREPLAYABLE_VAR_1,64)}" cannot be handed to a teammate intact, so the teammate was not started. Remove that rule or move it to permissions.deny in settings, then try again.
