<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable, bind the positional
  (suggestion)
description: >-
  Remedy clause spliced into the unset-variable dangerous-removal refusal when
  the target uses a positional parameter: bind it (and rewrite any named
  variables with a :? guard), single-quoting an inline sh -c script, or use a
  literal absolute path.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_BIND_POSITIONAL_SUGGESTION_VAR_0
-->
${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_BIND_POSITIONAL_SUGGESTION_VAR_0} (in an inline \`sh -c\` script, single-quote the script so this shell does not expand the positional) or use a literal absolute path
