<!--
name: Tool permission denied tool_use_error wrapper
description: >-
  tool_result content wrapping a deny message in a <tool_use_error> tag sent to
  the model; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_RESULT_PERMISSION_DENIED_WRAPPER_VAR_0
-->
<tool_use_error>${TOOL_RESULT_PERMISSION_DENIED_WRAPPER_VAR_0.denyMessage}</tool_use_error>
