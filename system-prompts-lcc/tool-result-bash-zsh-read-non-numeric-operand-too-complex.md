<!--
name: 'Tool Result: Bash Zsh Read Non-Numeric Operand Too Complex'
description: >-
  Bash too-complex reason when a zsh `read` numeric option operand is
  non-numeric, because zsh arith-evaluates it and may run $(cmd)
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0[u-1]}' operand '${TOOL_RESULT_BASH_ZSH_READ_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1}' is non-numeric — zsh arith-evals subscripts/expressions (may run $(cmd))
