<!--
name: Bash Cd Unresolved Deny Rule Names File
description: >-
  Permission-deny tool result when a command after an unresolvable cd reads a
  file named by a deny rule.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_0
  - TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_1
  - TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_2
-->
${TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_0[0]} reads '${TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_1}' after a cd whose target cannot be resolved, and a deny rule (${TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_2.ruleValue.ruleContent??TOOL_RESULT_BASH_CD_UNRESOLVED_DENY_RULE_NAMES_FILE_VAR_2.ruleValue.toolName}) names that file under a directory it may run in
