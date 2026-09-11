<!--
name: 'Tool Parameter: Monitor Timeout Capped Re-arm'
description: >-
  Describes Monitor timeout_ms when persistent mode is unavailable: deadlines
  cap at a maximum and the model is notified so it can re-arm.
ccVersion: 2.1.268
variables:
  - TOOL_PARAMETER_MONITOR_TIMEOUT_CAPPED_REARM_VAR_0
  - TOOL_PARAMETER_MONITOR_TIMEOUT_CAPPED_REARM_VAR_1
-->
Kill the monitor after this deadline. Default ${TOOL_PARAMETER_MONITOR_TIMEOUT_CAPPED_REARM_VAR_0}ms. Deadlines above ${TOOL_PARAMETER_MONITOR_TIMEOUT_CAPPED_REARM_VAR_1}ms are capped to ${TOOL_PARAMETER_MONITOR_TIMEOUT_CAPPED_REARM_VAR_1}ms. You are notified at expiry and can re-arm.
