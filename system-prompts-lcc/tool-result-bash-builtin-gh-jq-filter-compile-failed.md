<!--
name: 'Tool Result: Bash built-in gh --jq filter failed to compile'
description: >-
  Built-in gh api stderr when the local jq cannot compile the --jq filter; no
  request was sent.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_COMPILE_FAILED_VAR_0
  - TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_COMPILE_FAILED_VAR_1
-->
${TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_COMPILE_FAILED_VAR_0(TOOL_RESULT_BASH_BUILTIN_GH_JQ_FILTER_COMPILE_FAILED_VAR_1.stderr)}gh: no request was sent: the jq on this machine could not compile the --jq filter. Change the filter, or run the command without --jq and pipe the output to a JSON tool that is installed.
