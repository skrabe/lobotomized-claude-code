<!--
name: 'Tool Result: remote host unresponsive despite liveness check'
description: >-
  Explains that an attached/remote host is still connected but stopped answering
  a command, its state is unknown, and instructs Claude not to re-run
  non-idempotent commands and to tell the user what could not be verified
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_1
  - TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_2
  - TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_3
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_0} is still connected, but its reply to this command was not received (${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_1} checks about ${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_2.round(TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_3/1000)} s apart got no answer, though ${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_0} answered a liveness check). Its state is unknown — it may have completed, failed, or still be running; the reply may have been too large to deliver. Do not re-run non-idempotent commands on ${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_0} just to see the output. If the output may be large, try a narrower command (part of a file, a filter, or a smaller image); otherwise do the rest of the task without ${TOOL_RESULT_REMOTE_TOOL_HOST_UNRESPONSIVE_LIVENESS_CHECKED_VAR_0}, and tell the user what you could not verify.
