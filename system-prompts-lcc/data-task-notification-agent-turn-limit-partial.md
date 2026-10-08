<!--
name: 'Data: task notification agent turn limit partial'
description: >-
  Task-notification status when a background agent stops at its turn limit with
  a partial result, optionally followed by the continue hint.
ccVersion: 2.1.294
variables:
  - DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_0
  - DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_1
  - DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_2
-->
stopped at its ${DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_0}-turn limit (partial result${DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_1===!1?"":DATA_TASK_NOTIFICATION_AGENT_TURN_LIMIT_PARTIAL_VAR_2})
