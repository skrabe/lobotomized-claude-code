<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable removes a top-level
  dir, add :? guard (suggestion)
description: >-
  Remedy clause in the dangerous-removal ask message that suggests a `${VAR:?}`
  guard rewrite, so the shell stops with an error instead of removing a
  top-level directory when the variable is unset or empty.
ccVersion: 2.1.281
variables:
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_0
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_1
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_2
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_3
-->
rewrite it as ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_0}${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_1}${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_0}, which makes the shell stop with an error instead of removing /${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_2.rootChild} when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_SUGGESTION_VAR_3} is unset or empty (it is not set in the environment this command inherits), or use a literal absolute path
