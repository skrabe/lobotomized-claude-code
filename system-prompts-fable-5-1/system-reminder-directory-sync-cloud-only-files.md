<!--
name: 'System Reminder: Directory Sync Cloud-Only Files'
description: >-
  Reminds the model that listed files exist only in the cloud checkout and are
  never sent to the user's machine.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_0
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_1
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_2
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_3
-->
Directory sync: these files exist only in this cloud checkout and are NOT sent to the user's machine (untracked files under dot-led paths or dependency/build-output directories, editor or temporary files, and files with credential-like or otherwise withheld names never travel): ${[SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_0([...SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_1.credentialNamed,...SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_1.named]),SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_2].filter(SYSTEM_REMINDER_DIRECTORY_SYNC_CLOUD_ONLY_FILES_VAR_3).join(", ")}. If the user needs them on their machine, tell them so plainly.
