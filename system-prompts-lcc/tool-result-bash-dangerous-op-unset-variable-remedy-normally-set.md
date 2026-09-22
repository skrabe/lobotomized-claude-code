<!--
name: 'Tool Result: Bash Dangerous Op Remedy — Normally-Set Variable'
description: >-
  Remedy clause in the dangerous-removal ask message when the target's variable
  (e.g. $HOME, $TMPDIR) is normally set, so a :? guard would not stop it; tells
  the model to use a literal absolute path.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_REMEDY_NORMALLY_SET_VAR_0
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_REMEDY_NORMALLY_SET_VAR_1
-->
use a literal absolute path: ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_REMEDY_NORMALLY_SET_VAR_0} is normally set, so a guard on it would not stop this ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VARIABLE_REMEDY_NORMALLY_SET_VAR_1}
