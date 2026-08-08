<!--
name: 'Tool Result: SendMessage device-gated session reply-only'
description: >-
  SendMessage tool result returned when the recipient name resolves to a
  device-gated (bridge reply-only) session that cannot be addressed by name from
  this machine.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_1
  - TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_2
  - TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_3
-->
'${TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_0.to}' matches a ${TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_1} session on this account, and those are reply-only from here: messageable ${TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_2}. The Claude Code Remote send_message connector is not a workaround either — it cannot reach these device-gated sessions, and its "untrusted device" error is misleading (this device is not the problem). If that session is who you meant, it isn't reachable by name from this machine; if you meant a different agent, ${TOOL_RESULT_SEND_MESSAGE_DEVICE_GATED_REPLY_ONLY_VAR_3}.
