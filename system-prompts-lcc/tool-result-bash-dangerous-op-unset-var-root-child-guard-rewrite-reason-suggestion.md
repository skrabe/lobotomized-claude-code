<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable removes a top-level
  dir, guard rewrite (short reason form)
description: >-
  Short decision-reason remedy used when an empty variable would remove a
  top-level directory. It suggests the guarded rewrite or a literal path.
ccVersion: 2.1.281
variables:
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_0
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_1
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_2
-->
rewrite it as ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_0} or use a literal path: when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_1} is empty this removes /${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_GUARD_REWRITE_REASON_SUGGESTION_VAR_2.rootChild}
