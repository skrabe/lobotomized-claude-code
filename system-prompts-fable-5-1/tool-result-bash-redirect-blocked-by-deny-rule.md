<!--
name: 'Tool Result: Bash redirect blocked by deny rule'
description: >-
  checkPermissions deny message when an env-wrapped command reads from or writes
  to a path a deny rule blocks.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_0
  - TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_1
  - TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_2
-->
${TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_0.argv[0]} ${TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_1==="read"?"from":"to"} '${TOOL_RESULT_BASH_REDIRECT_BLOCKED_BY_DENY_RULE_VAR_2}' was blocked by a deny rule.
