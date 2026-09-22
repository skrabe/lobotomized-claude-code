<!--
name: 'Tool Result: Bash Integer-Attribute Assignment Too Complex'
description: >-
  Ask-path tool_result when an integer-attribute assignment would arith-eval the
  RHS and may run command substitution.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_BASH_INTEGER_ATTRIBUTE_ASSIGNMENT_TOO_COMPLEX_VAR_0
-->
${TOOL_RESULT_BASH_INTEGER_ATTRIBUTE_ASSIGNMENT_TOO_COMPLEX_VAR_0.name} has integer attribute — assignment arith-evals RHS, which can execute subscript command substitution or abort/diverge at runtime
