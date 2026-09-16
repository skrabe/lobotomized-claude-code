<!--
name: >-
  Tool Result: Bash dangerous operation — glob traverses unenumerable
  directories
description: >-
  Refusal the model reads when a destructive bash command's glob pattern
  traverses directories that cannot be statically enumerated; it states the
  action needs explicit approval and cannot be auto-allowed by a permission
  rule.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_GLOB_TRAVERSES_UNENUMERABLE_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_GLOB_TRAVERSES_UNENUMERABLE_VAR_1
-->
Dangerous ${TOOL_RESULT_BASH_DANGEROUS_OP_GLOB_TRAVERSES_UNENUMERABLE_VAR_0} operation detected: '${TOOL_RESULT_BASH_DANGEROUS_OP_GLOB_TRAVERSES_UNENUMERABLE_VAR_1}'

This command's glob pattern traverses directories that cannot be statically enumerated. This requires explicit approval and cannot be auto-allowed by permission rules.
