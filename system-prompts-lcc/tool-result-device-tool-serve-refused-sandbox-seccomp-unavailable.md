<!--
name: 'Device tool refused: sandbox seccomp unavailable'
description: >-
  Refusal message for a served device-tool call explaining the sandbox found no
  runnable seccomp filter helper to block Unix-socket connections, so the device
  serves no device tools; ask the user to check /sandbox and restart.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_DEVICE_TOOL_SERVE_REFUSED_SANDBOX_SECCOMP_UNAVAILABLE_VAR_0
-->
${TOOL_RESULT_DEVICE_TOOL_SERVE_REFUSED_SANDBOX_SECCOMP_UNAVAILABLE_VAR_0} refused: the sandbox on this device cannot block connections to Unix sockets because the sandbox runtime found no seccomp filter helper it could run, so a command could reach services running outside the sandbox, and this device serves no device tools. Ask the user to open /sandbox on the device (its Dependencies tab shows the seccomp filter's status) and restart Claude Code there once it is fixed; do not retry until they have.
