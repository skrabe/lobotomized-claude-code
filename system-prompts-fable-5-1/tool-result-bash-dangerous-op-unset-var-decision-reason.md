<!--
name: 'Tool Result: Bash dangerous operation — unset variable decision reason'
description: >-
  Decision-reason suffix for the unset-variable dangerous-removal safety check.
  It becomes 'Dangerous <cmd> operation on possibly-empty variable path…' and
  names the target, the command and the short remedy.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_2
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_3
-->
on possibly-empty variable path${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_0?" inside command substitution":""}: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_1} in \`${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_2}\` (${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_3(!1)})
