<!--
name: 'Tool Result: SendFile device-gated session reply-only'
description: >-
  SendFile refusal text returned as the tool result when the target name
  resolves to a device-gated cloud/local session that cannot receive files by
  name from this machine.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_0
  - TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_1
  - TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_2
  - TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_3
-->
'${TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_0}' matches a ${TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_1} session on this account; those are reply-only from here (a message ${TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_2}) and files can't be sent to them by name from this machine. The Claude Code Remote send_message connector is not a workaround either — it cannot reach these device-gated sessions, and its "untrusted device" error is misleading. If that session is who you meant, it isn't reachable by name from this machine; if you meant a different agent, ${TOOL_RESULT_SENDFILE_DEVICE_GATED_REPLY_ONLY_VAR_3}.
