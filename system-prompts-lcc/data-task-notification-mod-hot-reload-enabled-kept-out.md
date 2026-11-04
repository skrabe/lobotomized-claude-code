<!--
name: 'Data: Task notification mod hot-reload enabled, hooks kept out'
description: >-
  Notification telling Claude that mod hot-reloading was enabled but the mods'
  hooks modules did not load (kept out), with the cause.
ccVersion: 2.1.318
variables:
  - DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_KEPT_OUT_VAR_0
  - DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_KEPT_OUT_VAR_1
-->
The person enabled mod hot-reloading for this session, but the hooks modules of the mods under ${DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_KEPT_OUT_VAR_0} had NOT loaded when this notice was written. They count as a person's hooks modules, not an organization's. The reason: ${DATA_TASK_NOTIFICATION_MOD_HOT_RELOAD_ENABLED_KEPT_OUT_VAR_1.cause}. You get no further notice about them, so do not say they are running, and /reload-plugins does not load them sooner. A mod with no hooks module did load.
