<!--
name: Host Did Not Reconnect
description: >-
  Tool-hosts notice telling the model not to do a machine's work locally after
  it failed to reconnect.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_3
-->
${SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_0} ${SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_1.join(", ")}. This session's cloud worker was replaced, and the Claude Code on ${SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_2} did not connect to the new one within ${SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_3} s. Do not do the work of ${SYSTEM_REMINDER_TOOL_HOSTS_DID_NOT_RECONNECT_VAR_2} here in this session's own environment, and do not report it as done: tell the user that it has not reconnected, and carry on only with work that does not need it. If it reconnects, its tools appear here again.
