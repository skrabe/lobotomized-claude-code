<!--
name: 'Tool Result: Send Message UDS Non-Local IPC Path'
description: >-
  UdsSendRefusedError message interpolated into the SendMessage local-socket
  failure tool result when the target path is not a usable local IPC path.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_SEND_MESSAGE_UDS_NON_LOCAL_IPC_PATH_VAR_0
-->
Refusing to connect: not a usable local IPC path (remote/UNC host, or a pipe name with extra segments or a trailing dot/space): ${TOOL_RESULT_SEND_MESSAGE_UDS_NON_LOCAL_IPC_PATH_VAR_0}
