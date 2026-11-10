<!--
name: Plugin dev mods unbound reload notice
description: >-
  Task notification telling the model that hot-reloaded plugin mods under a
  folder did not load because this session cannot reload its plugins (only a
  restart loads them).
ccVersion: 2.1.322
variables:
  - DATA_TASK_NOTIFICATION_PLUGIN_DEV_MODS_UNBOUND_VAR_0
  - DATA_TASK_NOTIFICATION_PLUGIN_DEV_MODS_UNBOUND_VAR_1
-->
${DATA_TASK_NOTIFICATION_PLUGIN_DEV_MODS_UNBOUND_VAR_0} mod hot-reloading for this session, but the mods under ${DATA_TASK_NOTIFICATION_PLUGIN_DEV_MODS_UNBOUND_VAR_1} did not load (this session cannot reload its plugins; only a restart loads them).
