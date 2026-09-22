<!--
name: 'Data: Directory sync trash restore failed'
description: >-
  Residue from ct() joined into the unfinished-checkout dir_sync_notice listing
  paths that could not be moved back from session trash.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_TRASH_RESTORE_FAILED_VAR_0
-->
${DATA_DIR_SYNC_TRASH_RESTORE_FAILED_VAR_0.length} file(s) could not be moved back from the session trash: ${DATA_DIR_SYNC_TRASH_RESTORE_FAILED_VAR_0.slice(0,10).join(", ")}
