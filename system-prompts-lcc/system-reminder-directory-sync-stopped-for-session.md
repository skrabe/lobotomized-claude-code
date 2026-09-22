<!--
name: 'System Reminder: Directory sync stopped for session'
description: >-
  Reports that directory sync permanently stopped, explains the local
  synced-copy disposition and any unsynced files, and directs all project work
  to the user's attached machine
ccVersion: 2.1.251
variables:
  - ESCAPE_UNTRUSTED_TEXT_FN
  - SYNC_STOP_REASON
  - LOCAL_SYNC_COPY_DISPOSITION
  - REMOTE_MACHINE_FIELD_NAME
  - UNSYNCED_CHANGES_NOTE
-->
Directory sync has STOPPED for this session and will not resume in it — the user's machine reported: "${ESCAPE_UNTRUSTED_TEXT_FN(SYNC_STOP_REASON)}". So that you and the user never work on two different versions of the project, ${LOCAL_SYNC_COPY_DISPOSITION} Nothing was changed on the user's machine — it has all of the user's files and everything of yours that reached it. From now on the project's files live ONLY on the user's machine: run commands there and read, edit and write files there by adding "${REMOTE_MACHINE_FIELD_NAME}": "<that machine>" to Bash, Read, Edit and Write calls (the attached-machines note names the machine and its project directory; use absolute paths there); use this environment only for scratch work that needs none of the project's files, do not recreate project files here, and stop any background command you started here that uses the project. If that machine is not reachable for tools, tell the user plainly that you cannot reach their files until it reconnects.${UNSYNCED_CHANGES_NOTE} Tell the user in one or two sentences that file sync stopped and why, and that you are continuing directly on their machine.
