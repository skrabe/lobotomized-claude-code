<!--
name: Device hook program writable by cloud
description: Refusal when the hook program resolves to a file the cloud session can write.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_0
  - TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_1
  - TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_2
-->
not run — ${TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_0===TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_1?TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_0:"its program"} on ${TOOL_RESULT_DEVICE_HOOK_PROGRAM_IN_REACH_VAR_2.displayName} leads to a file the cloud session can write
