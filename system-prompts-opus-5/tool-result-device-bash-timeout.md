<!--
name: 'Tool Result: Device Bash Timeout'
description: >-
  Returned as an error tool result when a device_bash command is stopped after
  exceeding its timeout.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_DEVICE_BASH_TIMEOUT_VAR_0
  - TOOL_RESULT_DEVICE_BASH_TIMEOUT_VAR_1
-->
${TOOL_RESULT_DEVICE_BASH_TIMEOUT_VAR_0}

The command was stopped on the device because it did not finish within ${TOOL_RESULT_DEVICE_BASH_TIMEOUT_VAR_1} ms; it may have partially completed. Do not retry non-idempotent commands.
