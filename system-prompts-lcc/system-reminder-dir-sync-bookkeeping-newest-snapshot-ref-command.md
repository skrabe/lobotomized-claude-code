<!--
name: 'System Reminder: Dir Sync Bookkeeping Newest Snapshot Ref Command'
description: >-
  Fragment of the bookkeeping-commit reminder giving the git for-each-ref
  command that prints the newest received snapshot ref to compare against.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_NEWEST_SNAPSHOT_REF_COMMAND_VAR_0
-->
\`git for-each-ref --sort=-version:refname --count=1 --format='%(refname)' ${SYSTEM_REMINDER_DIR_SYNC_BOOKKEEPING_NEWEST_SNAPSHOT_REF_COMMAND_VAR_0.receivedSnapshotsPrefix}\` prints the ref of the newest snapshot of them — run it when you act, since a newer one may have arrived from the user's machine after this was written, and if it prints nothing, none is held here and this check does not apply
