<!--
name: 'Remote Tool: Ask Rule Keyed On Machine Argument'
description: >-
  Session-rule refusal when an ask rule matches the machine argument itself,
  which this session cannot honour as a prompt.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_2
-->
The rule ${TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_0.ruleValue.toolName}(${TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_0.ruleValue.ruleContent}) asks for approval keyed on the machine argument itself, which this session cannot honour as a prompt — use a deny rule for the machine (or, for every attached machine whatever it calls itself, a rule on mcp__${TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_1}), an ordinary ask rule for the command, or remove it to let ${TOOL_RESULT_REMOTE_TOOL_ASK_RULE_ON_MACHINE_ARG_VAR_2.name}'s own Claude Code decide.
