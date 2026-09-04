<!--
name: 'Tool Result: Bash Double-Bracket Non-Numeric Operand Too Complex'
description: >-
  Ask-path tool_result when a [[ ]] operand is non-numeric and would arith-eval
  identifiers or subscripts.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'${TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0} ... ${TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1[x]} ...' operand is non-numeric — \`[[\` arithmetically evaluates identifiers/subscripts (may run $(cmd))
