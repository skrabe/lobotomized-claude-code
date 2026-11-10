<!--
name: 'Tool Result: Bash built-in gh --jq failed after non-GET request was sent'
description: >-
  Built-in gh api stderr when a non-GET request was sent but --jq could not
  filter the response, warning that rerunning resends the request.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_FAILED_AFTER_SEND_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_FAILED_AFTER_SEND_VAR_1
-->
gh: the ${TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_FAILED_AFTER_SEND_VAR_0} was sent (last response: HTTP ${TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_FAILED_AFTER_SEND_VAR_1.status}), but --jq could not filter the response. Running the command again would send the ${TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_FAILED_AFTER_SEND_VAR_0} again.
