<!--
name: 'System Reminder: Dir Sync Update Record Not Taken'
description: >-
  Tells the cloud agent this turn's files uploaded but the sync service did not
  take the update record, so the user's machine has not received them yet; the
  record is retried and the user should be told the edits are delayed.
ccVersion: 2.1.265
-->
Directory sync: this turn's files were uploaded, but the sync service did not take this turn's update record, so the user's machine has not received them yet; the record is sent again at the next sync point (nothing is lost). If the user expects to see these edits on their machine now, say that they are delayed.
