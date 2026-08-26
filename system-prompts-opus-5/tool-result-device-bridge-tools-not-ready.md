<!--
name: 'Tool Result: Device Bridge Tools Not Ready'
description: >-
  Tells Claude the attached machine's tools could not be listed yet so the
  remote tool call did not run.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_0
  - TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_1
-->
The attached machine's tools could not be read yet — it may still be connecting, so "${TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_0(TOOL_RESULT_DEVICE_BRIDGE_TOOLS_NOT_READY_VAR_1)}" cannot be matched right now; the call did not run. Try again in a few seconds.
