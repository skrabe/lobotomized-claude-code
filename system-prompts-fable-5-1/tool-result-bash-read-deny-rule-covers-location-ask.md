<!--
name: Bash Read Deny Rule Covers Location Ask
description: >-
  Permission-ask message when the command would read a path covered by a deny
  rule and only the user can approve.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_0
  - TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_1
  - TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_2
  - TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_3
-->
${TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_0} on '${TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_1}' would read '${TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_2.location}', which the deny rule ${TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_3(TOOL_RESULT_BASH_READ_DENY_RULE_COVERS_LOCATION_ASK_VAR_2.rule.ruleValue)} covers; only you can approve running it anyway.
