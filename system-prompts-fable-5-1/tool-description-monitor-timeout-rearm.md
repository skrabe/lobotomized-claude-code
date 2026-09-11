<!--
name: 'Tool Description: Monitor Timeout Re-arm'
description: >-
  Explains that every monitor expires after timeout_ms, is killed with an
  event-count notice, and should be re-armed for long watches.
ccVersion: 2.1.268
variables:
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_0
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_1
  - TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_2
-->
Every monitor expires after \`timeout_ms\` (default ${TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_0(TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_1)}, at most ${TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_0(TOOL_DESCRIPTION_MONITOR_TIMEOUT_REARM_VAR_2())}): it is killed and you get one notice with the event count. Re-arm it if you still need the watch; for a long watch (PR monitoring, log tails) set \`timeout_ms\` to the maximum and re-arm on each expiry, and widen the filter if an expiry with no events was unexpected.
