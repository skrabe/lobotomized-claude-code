<!--
name: Bash Double-Bracket Non-Numeric Operand Too Complex
description: >-
  Bash too-complex reason when a [[ arithmetic operand is non-numeric and may
  run $(cmd) via identifier/subscript evaluation.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0
  - TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1
-->
'${TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_0} ... ${TOOL_RESULT_BASH_DOUBLE_BRACKET_NON_NUMERIC_OPERAND_TOO_COMPLEX_VAR_1[v]} ...' operand is non-numeric — \`[[\` arithmetically evaluates identifiers/subscripts (may run $(cmd))
