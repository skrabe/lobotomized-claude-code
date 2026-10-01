<!--
name: 'Tool Result: Tool input earlier option unavailable'
description: >-
  Appended to a tool InputValidationError when parameters or enum values the
  model used were offered earlier in the conversation but are not available in
  this session, telling it to continue without them
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_0
  - TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_1
-->
${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_0?TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_1[0]:`${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_1.slice(0,-1).join(", ")} and ${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_1.at(-1)}`} ${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_0?"was":"were"} offered earlier in this conversation but ${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_0?"is":"are"} not available in this session; continue without ${TOOL_RESULT_TOOL_INPUT_EARLIER_OPTION_UNAVAILABLE_VAR_0?"it":"them"}.
