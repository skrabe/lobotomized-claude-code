<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable expansion (refusal with
  remedy)
description: >-
  Refusal the model reads when a destructive bash command targets a shell
  variable expansion that becomes /, /* or a top-level path if the variable is
  unset or empty. It says the action needs explicit approval and cannot be
  auto-allowed by a permission rule, and it ends with a concrete remedy.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_2
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_3
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_4
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_5
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_0} operation detected in \`${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_1}\`${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_2?" (inside a command substitution)":""}. The target '${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_3}' is a shell variable expansion: when ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_4} is unset or empty it becomes \`/\`, \`/*\` or a top-level path. This requires explicit approval and cannot be auto-allowed by permission rules.

This check does not fire on a target that cannot expand to the filesystem root: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_EXPANSION_EXAMPLE_VAR_5(!0)}.
