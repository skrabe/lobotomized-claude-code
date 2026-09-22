<!--
name: No-such-tool error tool_result
description: >-
  tool_result content telling the model the requested tool is not available,
  wrapped in <tool_use_error>; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_NO_SUCH_TOOL_VAR_0
  - TOOL_RESULT_NO_SUCH_TOOL_VAR_1
-->
<tool_use_error>Error: No such tool available: ${TOOL_RESULT_NO_SUCH_TOOL_VAR_0}${TOOL_RESULT_NO_SUCH_TOOL_VAR_1}</tool_use_error>
