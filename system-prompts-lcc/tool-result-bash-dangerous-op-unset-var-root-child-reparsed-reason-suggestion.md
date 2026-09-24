<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable removes a top-level
  dir, re-parsed (short reason form)
description: >-
  Short decision-reason remedy used when an unset or empty variable would remove
  a top-level directory in a command that is parsed again. It tells the model to
  use a literal path.
ccVersion: 2.1.281
variables:
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_0
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_1
  - >-
    TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_2
-->
use a literal path: when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_0} is empty this removes /${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_1.rootChild}, and the ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_REASON_SUGGESTION_VAR_2} is parsed again before it runs
