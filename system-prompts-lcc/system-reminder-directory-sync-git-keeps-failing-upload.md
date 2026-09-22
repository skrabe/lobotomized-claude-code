<!--
name: Git Keeps Failing Upload
description: >-
  Directory-sync reminder telling the model this turn is on the last synced
  files because an upload keeps failing.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_GIT_KEEPS_FAILING_UPLOAD_VAR_0
-->
Directory sync: the user's newer changes are NOT here yet — git in this environment keeps failing to take in one of their machine's uploads (number ${SYSTEM_REMINDER_DIRECTORY_SYNC_GIT_KEEPS_FAILING_UPLOAD_VAR_0}), so this turn runs on the files as they last synced here; the upload is tried again at every turn. Say so if the user refers to changes you cannot see here.
