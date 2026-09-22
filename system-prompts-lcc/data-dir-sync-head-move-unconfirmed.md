<!--
name: 'Data: Directory sync HEAD move unconfirmed'
description: >-
  Residue sentence joined into the unfinished-checkout dir_sync_notice when git
  declined or could not confirm the planned HEAD move.
ccVersion: 2.1.246
variables:
  - DATA_DIR_SYNC_HEAD_MOVE_UNCONFIRMED_VAR_0
  - DATA_DIR_SYNC_HEAD_MOVE_UNCONFIRMED_VAR_1
-->
HEAD was meant to move from ${DATA_DIR_SYNC_HEAD_MOVE_UNCONFIRMED_VAR_0.head} to ${DATA_DIR_SYNC_HEAD_MOVE_UNCONFIRMED_VAR_1.targetHead}; git declined the move or its outcome could not be confirmed, so HEAD may stand at either
