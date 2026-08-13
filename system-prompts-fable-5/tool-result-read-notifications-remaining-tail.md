<!--
name: 'Tool Result: ReadNotifications Remaining Tail'
description: >-
  Continuation text telling the model how many queued notifications remain and
  to call ReadNotifications again.
ccVersion: 2.1.231
variables:
  - TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_0
  - TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_1
  - TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_2
-->


${TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_0} more ${TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_1(TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_0,"notification")} still queued — call ${TOOL_RESULT_READ_NOTIFICATIONS_REMAINING_TAIL_VAR_2} again to read the rest.
