<!--
name: 'Remote Tool: Bridge Rule This Session Cannot Check'
description: >-
  Refusal when a bridge-name rule cannot be checked field-by-field (command
  pattern or machine field), so every forwarded call of that tool is refused.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_3
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_4
-->
${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_0(TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_1.name,TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_2)} Rules on the bridge's names apply to a forwarded call field by field, and one this session cannot check that way (a pattern over the command, or the machine field) refuses every forwarded ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_1.name}: ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_1.name}(…) scopes a rule to commands, ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_1.name}(${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_3}:…) to one machine, and a plain rule on mcp__${TOOL_RESULT_REMOTE_TOOL_BRIDGE_UNCHECKABLE_RULE_VAR_4} covers every attached machine whatever it calls itself.
