<!--
name: Ripgrep search timed out
description: >-
  Grep/search tool error returned to the model when ripgrep exceeds the time
  budget.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_GREP_RIPGREP_TIMEOUT_VAR_0
-->
Ripgrep search timed out after ${TOOL_RESULT_GREP_RIPGREP_TIMEOUT_VAR_0()==="wsl"?60:20} seconds. The search may have matched files but did not complete in time. Try searching a more specific path or pattern.
