<!--
name: Monitor Started Expiry Rearm Clause
description: >-
  Expiry clause of the Monitor tool_result telling the model the watch ends
  unless re-armed.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_MONITOR_STARTED_EXPIRY_REARM_CLAUSE_VAR_0
  - TOOL_RESULT_MONITOR_STARTED_EXPIRY_REARM_CLAUSE_VAR_1
-->
expires in ${TOOL_RESULT_MONITOR_STARTED_EXPIRY_REARM_CLAUSE_VAR_0(TOOL_RESULT_MONITOR_STARTED_EXPIRY_REARM_CLAUSE_VAR_1.timeoutMs,{hideTrailingZeros:!0})} unless the source ends first; you get one notice at expiry — re-arm if you still need the watch
