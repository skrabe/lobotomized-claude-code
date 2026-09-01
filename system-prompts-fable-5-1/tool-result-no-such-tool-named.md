<!--
name: No-such-tool error (named) tool_result
description: >-
  tool_result content telling the model a named tool is not available, wrapped
  in <tool_use_error>; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_NO_SUCH_TOOL_NAMED_VAR_0
  - TOOL_RESULT_NO_SUCH_TOOL_NAMED_VAR_1
-->
<tool_use_error>Error: No such tool available: ${TOOL_RESULT_NO_SUCH_TOOL_NAMED_VAR_0.name}${TOOL_RESULT_NO_SUCH_TOOL_NAMED_VAR_1}</tool_use_error>
