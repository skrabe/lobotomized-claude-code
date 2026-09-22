<!--
name: 'Tool Result: Device Hook Changed Since Registered'
description: >-
  PreToolUse deny reason when the hook file changed on the attached machine
  since it was registered.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_CHANGED_SINCE_REGISTERED_VAR_0
-->
not run — its file changed on ${TOOL_RESULT_DEVICE_HOOK_CHANGED_SINCE_REGISTERED_VAR_0.displayName} since it was registered; it runs again once that machine re-registers it
