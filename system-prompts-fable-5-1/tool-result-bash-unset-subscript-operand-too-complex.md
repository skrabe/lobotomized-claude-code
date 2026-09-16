<!--
name: 'Tool Result: Bash Unset Subscript Operand Too Complex'
description: >-
  Too-complex reason when an unset operand carries a subscript that bash and zsh
  would evaluate.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_UNSET_SUBSCRIPT_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_UNSET_SUBSCRIPT_OPERAND_TOO_COMPLEX_VAR_1
-->
${TOOL_RESULT_BASH_UNSET_SUBSCRIPT_OPERAND_TOO_COMPLEX_VAR_0[0]??"unset"} operand ${TOOL_RESULT_BASH_UNSET_SUBSCRIPT_OPERAND_TOO_COMPLEX_VAR_1.text} carries a subscript — bash and zsh evaluate $(cmd) inside it
