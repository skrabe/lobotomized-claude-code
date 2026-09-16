<!--
name: 'Tool Result: Bash Declare Operand Not Plain Name Too Complex'
description: >-
  AST-walker too-complex reason when a declare/typeset/local operand is not a
  plain NAME with an inert value.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_1
  - TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_2
-->
${TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_0.children[0]?.TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_1??"declare"} operand '${TOOL_RESULT_BASH_DECLARE_OPERAND_NOT_PLAIN_NAME_TOO_COMPLEX_VAR_2.text}' is not a plain NAME with an inert value — the shell may re-parse it as a subscript, an expanded name or a compound assignment
