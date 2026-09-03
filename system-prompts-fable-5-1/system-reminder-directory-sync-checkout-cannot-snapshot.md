<!--
name: 'System Reminder: Directory sync checkout cannot snapshot'
description: >-
  Turn reminder that this turn's changes were not sent because the checkout
  cannot be snapshotted (merge/rebase/conflicts/unborn).
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_CANNOT_SNAPSHOT_VAR_0
-->
Directory sync: this turn's changes were NOT sent to the user's machine because this checkout cannot be snapshotted: ${SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_CANNOT_SNAPSHOT_VAR_0}. Nothing of yours reaches the user until that is resolved (finish or abort the operation, resolve and commit); do not tell the user their files have arrived — say they are held here until then.
