<!--
name: Remote Tool Or Do It Through Served Tool
description: >-
  Optional clause on the host-does-not-serve tool_result listing tools that host
  does serve, so the model can retry without the missing tool.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_REMOTE_TOOL_OR_DO_IT_THROUGH_SERVED_TOOL_VAR_0
  - TOOL_RESULT_REMOTE_TOOL_OR_DO_IT_THROUGH_SERVED_TOOL_VAR_1
-->
 — or do it on ${TOOL_RESULT_REMOTE_TOOL_OR_DO_IT_THROUGH_SERVED_TOOL_VAR_0} through a tool it does serve there (${TOOL_RESULT_REMOTE_TOOL_OR_DO_IT_THROUGH_SERVED_TOOL_VAR_1.join(", ")})
