<!--
name: 'System Reminder: Remote Machine File Sync Timing'
description: >-
  Main-conversation branch of remote-machine file-sync timing: when edits land,
  how inbound changes arrive, and to read ignored or unsynced files on the
  remote host.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0
  - SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_1
  - SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_2
-->
- File sync timing: edit here, in the synced copy; your edits reach ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0} at the end of your turn and just before each call you run on ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0}. What a call you run on ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0} creates or changes there ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_1} If ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0} cannot send it now, you are told so and what to expect. Edits the user makes on ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0} during your turn can also arrive between your tool calls, with a notice. Files git ignores never cross either way — read those, and anything not yet here, on ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_0} itself (have the command print it, or ${SYSTEM_REMINDER_REMOTE_MACHINE_FILE_SYNC_TIMING_VAR_2}).
