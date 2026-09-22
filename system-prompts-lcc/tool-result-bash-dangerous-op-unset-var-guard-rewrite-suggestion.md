<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable, add :? guard
  (suggestion)
description: >-
  Remedy clause in the unset-variable dangerous-removal refusal offering two
  fixes: rewrite the command with ${VAR:?} guards, so the shell stops with an
  error instead of running the removal when the variable is unset or empty, or
  use a literal absolute path.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_2
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_3
-->
rewrite it as ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_0}${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_1}${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_0}, which makes the shell stop with an error instead of running ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_2} when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_GUARD_REWRITE_SUGGESTION_VAR_3} is unset or empty, or use a literal absolute path
