<!--
name: 'System reminder: container restart untold agents stopped'
description: >-
  Notice that after a container restart the listed agents are stopped and were
  not resumed so the new message is read first.
ccVersion: 2.1.331
variables:
  - SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_STOPPED_VAR_0
  - SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_STOPPED_VAR_1
-->
The container was restarted. These agents are stopped, and were not resumed, so that you read the new message first: ${SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_STOPPED_VAR_0.join(", ")}. ${SYSTEM_REMINDER_CONTAINER_RESTART_UNTOLD_AGENTS_STOPPED_VAR_1}
