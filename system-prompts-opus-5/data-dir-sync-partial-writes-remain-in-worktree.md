<!--
name: 'Data: Directory sync partial writes remain in worktree'
description: >-
  Residue from Cl() joined into the unfinished-checkout dir_sync_notice listing
  paths that could not be moved to session trash.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_PARTIAL_WRITES_REMAIN_IN_WORKTREE_VAR_0
-->
${DATA_DIR_SYNC_PARTIAL_WRITES_REMAIN_IN_WORKTREE_VAR_0.length} partly written file(s) could not be moved to the session trash and remain in the working tree: ${DATA_DIR_SYNC_PARTIAL_WRITES_REMAIN_IN_WORKTREE_VAR_0.slice(0,10).join(", ")}
