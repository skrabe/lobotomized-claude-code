<!--
name: 'Tool Result: Bash Zsh Read Fused Non-Numeric Operand Too Complex'
description: >-
  Ask-path tool_result when a numeric operand fused into a zsh read flag (e.g.
  -t5x) may arith-eval and run command substitution.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_BASH_ZSH_READ_FUSED_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_FUSED_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_FUSED_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0}' (fused in '${TOOL_RESULT_BASH_ZSH_READ_FUSED_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1}') operand is non-numeric — zsh arith-evals subscripts/expressions (may run $(cmd))
