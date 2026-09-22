<!--
name: 'Tool Result: Bash Guard — Unset Target Not Statically Known'
description: >-
  Static bash-analysis refusal reason when a wrapped unset/unsetenv targets a
  variable whose value is no longer statically known; delivered to the model as
  the Bash tool_result error content on a non-allow permission decision.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_BASH_UNSET_VALUE_NOT_STATIC_WRAPPED_VAR_0
-->
'${TOOL_RESULT_BASH_UNSET_VALUE_NOT_STATIC_WRAPPED_VAR_0}' no longer has a statically known value at this unset (wrapped form) — cannot verify what the command leaves behind
