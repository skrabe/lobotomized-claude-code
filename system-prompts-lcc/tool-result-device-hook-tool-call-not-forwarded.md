<!--
name: 'Tool Result: Device Hook Tool Call Not Forwarded'
description: >-
  PreToolUse permissionDecisionReason denying a tool call whose input could not
  be forwarded to the attached machine.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_0
  - TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_1
  - TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_2
-->
[hook on ${TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_0.registry.current()?.TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_1??"your machine"}]: not run — the tool call ${TOOL_RESULT_DEVICE_HOOK_TOOL_CALL_NOT_FORWARDED_VAR_2?"is too large to forward to the attached machine; retry with a smaller input":"could not be forwarded to the attached machine; retry with plain input"}
