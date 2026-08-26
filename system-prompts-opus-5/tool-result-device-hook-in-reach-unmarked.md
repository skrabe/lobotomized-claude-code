<!--
name: 'Tool Result: Device Hook In Reach Unmarked'
description: >-
  PreToolUse deny reason when a device hook file sits in a cloud-writable path
  and is not marked cloud: "device".
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_IN_REACH_UNMARKED_VAR_0
-->
not run — its file now sits where the cloud session can write on ${TOOL_RESULT_DEVICE_HOOK_IN_REACH_UNMARKED_VAR_0.displayName} and it is not marked cloud: "device"
