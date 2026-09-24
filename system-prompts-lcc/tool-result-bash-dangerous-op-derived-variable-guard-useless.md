<!--
name: >-
  Tool Result: Bash dangerous operation — variable derived in-command, guard
  does not help
description: >-
  Dangerous-removal ask message for a command that sets the target variable from
  an expression (such as dirname or cd && pwd) that can resolve to a directory.
  It says a `:?` guard would not help and asks for a literal absolute path.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_1
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_2
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_3
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_4
  - TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_5
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_0} operation detected in \`${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_1}\`${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_2}. This command sets $${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_3} from \`${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_4}\`, which ${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_5}, so this ${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_0} can remove that directory. A \`\${${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_3}:?}\` guard does not help, because $${TOOL_RESULT_BASH_DANGEROUS_OP_DERIVED_VARIABLE_GUARD_USELESS_VAR_3} is not empty. This requires explicit approval and cannot be auto-allowed by permission rules.

Use a literal absolute path instead.
