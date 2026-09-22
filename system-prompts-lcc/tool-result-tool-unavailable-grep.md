<!--
name: 'Tool unavailable, use grep note'
description: >-
  Injected note telling the model a tool is unavailable and to search contents
  with grep via the given tool.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_TOOL_UNAVAILABLE_GREP_VAR_0
  - TOOL_RESULT_TOOL_UNAVAILABLE_GREP_VAR_1
-->
. ${TOOL_RESULT_TOOL_UNAVAILABLE_GREP_VAR_0} is not available in this session — search file contents with \`grep\` via the ${TOOL_RESULT_TOOL_UNAVAILABLE_GREP_VAR_1} tool instead.
