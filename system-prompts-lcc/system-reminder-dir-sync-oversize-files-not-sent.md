<!--
name: 'System Reminder: Directory sync oversize files not sent'
description: >-
  dir_sync_notice listing per-file oversize paths that were not synced to the
  user's machine and instructing the model to tell the user and keep large
  artefacts out of the tree.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_2
-->
Directory sync: these files are over the per-file size limit, so this turn's version of them is NOT synced to the user's machine (which keeps whatever it last had there — nothing, for a new file): ${SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_0}${SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_1.length>SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_2?` and ${SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_1.length-SYSTEM_REMINDER_DIR_SYNC_OVERSIZE_FILES_NOT_SENT_VAR_2} more`:""}. Tell the user if they matter; keep large artefacts out of the synced tree.
