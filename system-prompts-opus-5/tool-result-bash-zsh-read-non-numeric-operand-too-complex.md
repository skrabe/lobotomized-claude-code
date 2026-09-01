<!--
name: 'Tool Result: Bash Zsh Read Non-Numeric Operand Too Complex'
description: >-
  Ask-path tool_result when zsh read's numeric operand may arith-eval a
  subscript and run command substitution.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0[v-1]}' operand '${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1}' is non-numeric — zsh arith-evals subscripts/expressions (may run $(cmd))
