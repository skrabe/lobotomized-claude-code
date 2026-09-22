<!--
name: 'Tool Result: Bash ANSI-C Operand Subscript Too Complex'
description: >-
  AST-walker too-complex reason for a $'…' declaration operand that may hide a
  subscript.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_1
  - TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_2
-->
${TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_0.children[0]?.TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_1??TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_0.type} operand ${TOOL_RESULT_BASH_ANSI_C_OPERAND_SUBSCRIPT_TOO_COMPLEX_VAR_2.text} — a $'…' word the shell decodes, which may carry a subscript the parser cannot read
