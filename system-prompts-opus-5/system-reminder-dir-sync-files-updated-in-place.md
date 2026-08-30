<!--
name: 'System Reminder: Dir-Sync Files Updated In Place'
description: >-
  Between-tools dir-sync notice that files changed on the user's machine were
  updated here and must be re-read before editing.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_3
-->
While you were working, ${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_0===1?"1 file changed on the user's machine and was":`${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_0} files changed on the user's machine and were`} updated here to match${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_1.length===0?"":`: ${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_1.map(SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_2).join(", ")}${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_3>0?` and ${SYSTEM_REMINDER_DIR_SYNC_FILES_UPDATED_IN_PLACE_VAR_3} more`:""}`}. Re-read any of them you had read before you edit them.
