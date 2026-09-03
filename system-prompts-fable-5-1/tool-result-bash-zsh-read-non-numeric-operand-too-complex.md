<!--
name: Bash Zsh Read Non-Numeric Operand Too Complex
description: >-
  Bash too-complex reason when a zsh read numeric option's operand is
  non-numeric and may arith-eval $(cmd).
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0[T-1]}' operand '${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1}' is non-numeric — zsh arith-evals subscripts/expressions (may run $(cmd))
