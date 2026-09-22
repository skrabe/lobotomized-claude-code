<!--
name: 'WebFetch agents — nothing to check, relaunch'
description: >-
  Tail noting the WebFetch-launched agents left nothing to check, so they must
  be launched again.
ccVersion: 2.1.265
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RELAUNCH_TAIL_VAR_0
-->
 ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RELAUNCH_TAIL_VAR_0.length===1?"Agent":"Agents"} ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RELAUNCH_TAIL_VAR_0.join(", ")} fetched web content and ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RELAUNCH_TAIL_VAR_0.length===1?"has":"have"} nothing to check — launch ${DATA_TASK_NOTIFICATION_BACKGROUND_AGENTS_WEBFETCH_RELAUNCH_TAIL_VAR_0.length===1?"it":"them"} again if still needed.
