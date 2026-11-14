<!--
name: Host Not Reconnected Yet
description: >-
  Tool-hosts notice telling the model a replaced worker has not reconnected and
  not to report its work done.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_1
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_2
  - SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_3
-->
${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_0} ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_1.join(", ")}. This session's cloud worker was replaced, and the Claude Code on ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_2} has not connected to the new one yet. Do not do the work of ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_2} here in this session's own environment, and do not report it as done. ${SYSTEM_REMINDER_TOOL_HOSTS_NOT_RECONNECTED_YET_VAR_3}
