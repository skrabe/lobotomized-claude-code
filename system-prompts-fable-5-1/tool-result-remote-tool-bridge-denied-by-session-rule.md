<!--
name: 'Remote Tool: Bridge Denied By Session Rule'
description: >-
  Refusal when a deny rule on the bridge name blocks forwarding, so the tool is
  not sent to the host either.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_3
-->
The rule ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_0(TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_1.ruleValue)} denies this session the bridge that reaches ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_2.name}, so its ${TOOL_RESULT_REMOTE_TOOL_BRIDGE_DENIED_BY_SESSION_RULE_VAR_3.name} is not forwarded there either.
