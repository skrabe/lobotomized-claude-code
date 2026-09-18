<!--
name: 'Tool Result: Bash Zsh Read Prompt Subscript Too Complex'
description: >-
  Bash too-complex reason when a zsh `read -p` operand is a subscripted,
  dash-prefixed or runtime-determined NAME that zsh may arith-evaluate
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_1
-->
'read ${TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_0[u-1]}' operand '${TOOL_RESULT_BASH_ZSH_READ_PROMPT_SUBSCRIPT_TOO_COMPLEX_VAR_1}' is a subscripted NAME, dash-prefixed with a subscript, or runtime-determined — zsh -p takes no operand; may arith-eval the subscript and run $(cmd)
