<!--
name: Bash Zsh Read Prompt Subscript Too Complex
description: >-
  Permission-denial reason when a zsh read -p operand is subscripted or
  runtime-determined and may arith-eval.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_0[k-1]}' operand '${TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_1}' is a subscripted NAME, dash-prefixed with a subscript, or runtime-determined — zsh -p takes no operand; may arith-eval the subscript and run $(cmd)
