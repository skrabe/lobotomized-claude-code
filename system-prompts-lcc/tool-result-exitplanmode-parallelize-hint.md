<!--
name: ExitPlanMode parallelize hint
description: >-
  Text appended to the ExitPlanMode tool_result suggesting the agent spawn named
  teammates to parallelize independent tasks.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_EXITPLANMODE_PARALLELIZE_HINT_VAR_0
-->


If this plan can be broken down into multiple independent tasks, consider spawning named teammates with the ${TOOL_RESULT_EXITPLANMODE_PARALLELIZE_HINT_VAR_0} tool (pass a \`name\`) to parallelize the work.
