<!--
name: 'Tool result: agent restart not resumed'
description: >-
  An agent stopped by a container restart may have done some work and was not
  resumed, with the reason.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_AGENT_RESTART_NOT_RESUMED_ERROR_VAR_0
  - TOOL_RESULT_AGENT_RESTART_NOT_RESUMED_ERROR_VAR_1
-->
Agent ${TOOL_RESULT_AGENT_RESTART_NOT_RESUMED_ERROR_VAR_0} stopped when the container was restarted. It may have done some or all of its work by then. It was not resumed: ${TOOL_RESULT_AGENT_RESTART_NOT_RESUMED_ERROR_VAR_1}
