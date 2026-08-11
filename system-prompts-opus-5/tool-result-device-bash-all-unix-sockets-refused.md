<!--
name: 'Tool Result: Device Bash All Unix Sockets Refused'
description: >-
  Returned as an error tool result when the device sandbox permits all
  Unix-socket connections and cannot safely serve device_bash.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_DEVICE_BASH_ALL_UNIX_SOCKETS_REFUSED_VAR_0
-->
${TOOL_RESULT_DEVICE_BASH_ALL_UNIX_SOCKETS_REFUSED_VAR_0} refused: the sandbox on this device allows connections to every Unix socket (sandbox.network.allowAllUnixSockets), through which a command could reach services running outside the sandbox. Remove that setting on the device to use device_bash.
