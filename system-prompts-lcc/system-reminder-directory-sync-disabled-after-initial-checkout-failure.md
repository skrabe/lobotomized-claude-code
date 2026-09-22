<!--
name: 'System Reminder: Directory sync disabled after initial checkout failure'
description: >-
  Reports that directory sync is disabled after the initial checkout failed,
  states that the cloud working directory lacks the user's files, and directs
  project work to the attached machine
ccVersion: 2.1.251
variables:
  - SYNC_DISABLE_REASON
  - REMOTE_MACHINE_FIELD_NAME
-->
Directory sync is OFF for this session and the working directory does NOT hold the user's files: ${SYNC_DISABLE_REASON}. Tell the user plainly; their terminal is being told too, and it ends the session's file sync there. The project's files live only on the user's machine: if it is attached for tools (the attached-machines note names it and its project directory), run commands and read, edit and write files there by adding "${REMOTE_MACHINE_FIELD_NAME}": "<that machine>" to Bash, Read, Edit and Write calls; do not recreate project files here. If that machine is not reachable for tools, say that you cannot reach their files from this session.
