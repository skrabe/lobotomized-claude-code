<!--
name: 'System reminder: memory delete via rm full path'
description: >-
  Tells the model how to delete a file from shared memory: run a command that is
  only an rm of its full path under the mount directory.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MEMORY_DELETE_VIA_RM_FULL_PATH_VAR_0
  - SYSTEM_REMINDER_MEMORY_DELETE_VIA_RM_FULL_PATH_VAR_1
-->
To delete a file from shared memory, run a command that is only an rm of its full path under ${SYSTEM_REMINDER_MEMORY_DELETE_VIA_RM_FULL_PATH_VAR_0(SYSTEM_REMINDER_MEMORY_DELETE_VIA_RM_FULL_PATH_VAR_1.mountDir)}.
