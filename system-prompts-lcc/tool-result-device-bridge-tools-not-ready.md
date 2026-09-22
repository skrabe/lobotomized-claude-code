<!--
name: Device Bridge Tools Not Ready
description: >-
  Tool result when the attached machine's tools cannot be matched yet, so the
  call did not run.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_0
  - TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_1
-->
The attached machine's tools could not be read yet — it may still be connecting (or serving is switched off on it, or its announcement could not be verified by this session), so "${TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_0(TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_1)}" cannot be matched right now; the call did not run. Try again in a few seconds.
