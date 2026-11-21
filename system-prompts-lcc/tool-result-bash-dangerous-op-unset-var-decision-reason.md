<!--
name: 'Tool Result: Bash dangerous operation — unset variable decision reason'
description: >-
  Head of the decision-reason suffix for the unset-variable dangerous-removal
  safety check ('Dangerous <cmd> operation on possibly-empty variable path…'
  naming the target); the ` in `<cmd>` (<remedy>)` tail is now a separate
  template.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_1
-->
on possibly-empty variable path${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_0?" inside command substitution":""}: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_DECISION_REASON_VAR_1}
