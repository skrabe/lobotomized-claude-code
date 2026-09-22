<!--
name: >-
  Tool Result: Bash dangerous operation — unset variable re-parsed (short reason
  form)
description: >-
  Short remedy used in the decision reason of the unset-variable
  dangerous-removal check when the target is re-parsed (quoted string or eval):
  use a literal path.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_REPARSED_REASON_SUGGESTION_VAR_0
-->
use a literal path: the ${TOOL_RESULT_BASH_DANGEROUS_OP_UNSET_VAR_REPARSED_REASON_SUGGESTION_VAR_0} is parsed again before it runs
