<!--
name: 'Tool Result: Device Hook Changed While Writable'
description: >-
  PreToolUse deny reason when the hook file changed while the cloud session
  could write to it.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_DEVICE_HOOK_CHANGED_WHILE_WRITABLE_VAR_0
-->
not run — its file changed on ${TOOL_RESULT_DEVICE_HOOK_CHANGED_WHILE_WRITABLE_VAR_0.displayName} while the cloud session could write to it; review the file there before trusting it again
