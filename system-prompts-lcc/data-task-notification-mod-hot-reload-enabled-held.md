<!--
name: 'Task notification: mod hot-reload enabled but held'
description: >-
  Task-notification text telling Claude mod hot-reloading was enabled (by the
  person or the permission mode), but the mods under a given folder are held for
  /reload-plugins (since loading now would rewrite the prompt cache) and are NOT
  loaded yet.
ccVersion: 2.1.322
variables:
  - DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_HELD_VAR_0
  - DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_HELD_VAR_1
-->
${DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_HELD_VAR_0} mod hot-reloading for this session, but the mods under ${DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_HELD_VAR_1} wait for /reload-plugins (the load would rewrite the prompt cache): they are NOT loaded yet.
