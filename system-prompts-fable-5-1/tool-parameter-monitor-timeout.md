<!--
name: 'Tool Parameter: Monitor timeout_ms'
description: >-
  The timeout_ms param in the Monitor tool input schema setting the watch
  deadline; model-facing.
ccVersion: 2.1.191
variables:
  - TOOL_PARAMETER_MONITOR_TIMEOUT_VAR_0
  - TOOL_PARAMETER_MONITOR_TIMEOUT_VAR_1
-->
Kill the monitor after this deadline. Default ${TOOL_PARAMETER_MONITOR_TIMEOUT_VAR_0}ms, max ${TOOL_PARAMETER_MONITOR_TIMEOUT_VAR_1}ms. Ignored when persistent is true.
