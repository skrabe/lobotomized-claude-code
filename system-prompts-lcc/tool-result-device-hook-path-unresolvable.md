<!--
name: 'Tool Result: Device Hook Path Unresolvable'
description: >-
  PreToolUse permissionDecisionReason denying a tool call whose path could not
  be resolved for the attached machine.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_PATH_UNRESOLVABLE_VAR_0
  - TOOL_RESULT_DEVICE_HOOK_PATH_UNRESOLVABLE_VAR_1
-->
[hook on ${TOOL_RESULT_DEVICE_HOOK_PATH_UNRESOLVABLE_VAR_0.registry.current()?.TOOL_RESULT_DEVICE_HOOK_PATH_UNRESOLVABLE_VAR_1??"your machine"}]: not run — the path this tool call names could not be resolved for the attached machine; retry with a plain path
