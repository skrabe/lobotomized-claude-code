<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable removes a top-level
  dir, re-parsed (suggestion)
description: >-
  Remedy clause in the dangerous-removal ask message for this case: an unset or
  empty variable would remove a top-level directory, and the command is parsed
  again (quoted string or eval), so a guard would not protect it. It advises a
  literal absolute path.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_2
-->
use a literal absolute path: when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_0} is empty this ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_1} removes /${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_2.rootChild}, and the ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_ROOT_CHILD_REPARSED_SUGGESTION_VAR_1} is parsed again before it runs (it is inside a quoted string or after eval), so a pasted guard's quotes would not protect it
