<!--
name: 'System Reminder: Directory Sync Latest Not Uploaded'
description: >-
  Reminds the agent that its latest checkout changes were not uploaded to the
  user's machine until a later upload succeeds.
ccVersion: 2.1.257
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_LATEST_NOT_UPLOADED_VAR_0
-->
Directory sync: your latest changes were NOT uploaded to the user's machine — ${SYSTEM_REMINDER_DIRECTORY_SYNC_LATEST_NOT_UPLOADED_VAR_0.agentWords??SYSTEM_REMINDER_DIRECTORY_SYNC_LATEST_NOT_UPLOADED_VAR_0.words}. Nothing of yours reaches the user's machine until an upload from here goes through again (each upload carries everything that machine does not have yet). If the user expects these files on their machine now, say that they have not arrived.
