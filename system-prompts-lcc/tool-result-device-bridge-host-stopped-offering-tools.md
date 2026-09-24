<!--
name: 'Tool Result: Device bridge host stopped offering tools'
description: >-
  Tool-call error when Claude on the linked computer stopped offering its tools
  to the cloud session. It says nothing was sent and asks the model to have the
  user check or reopen Claude there, re-requesting folder access if needed.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_DEVICE_BRIDGE_HOST_STOPPED_OFFERING_TOOLS_VAR_0
  - TOOL_RESULT_DEVICE_BRIDGE_HOST_STOPPED_OFFERING_TOOLS_VAR_1
-->
"${TOOL_RESULT_DEVICE_BRIDGE_HOST_STOPPED_OFFERING_TOOLS_VAR_0(TOOL_RESULT_DEVICE_BRIDGE_HOST_STOPPED_OFFERING_TOOLS_VAR_1)}" cannot run anything for this session right now: Claude on that computer stopped offering its tools here (the Claude app there may have closed or lost its connection, or running tools for cloud sessions was switched off on it). Nothing was sent. Ask the user to check that Claude is running on that computer, and to open the Claude app there if it was closed; if this session got the computer by asking to use one of its folders, look the folders up and ask to use that folder again afterwards.
