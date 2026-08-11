<!--
name: 'Tool Result: Device Bash Sandbox Unconfined'
description: >-
  Returned as an error tool result when the device sandbox does not fully
  confine filesystem and network access.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_DEVICE_BASH_SANDBOX_UNCONFINED_VAR_0
-->
${TOOL_RESULT_DEVICE_BASH_SANDBOX_UNCONFINED_VAR_0} refused: the sandbox on this device is not fully confining (filesystem and network). Set "sandbox": {"enabled": true, "filesystem": {"disabled": false}} in Claude Code settings on the device, and do not run it in subprocess-env-scrub mode; then retry.
