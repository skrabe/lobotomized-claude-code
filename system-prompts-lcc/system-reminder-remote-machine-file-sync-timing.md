<!--
name: 'System Reminder: Remote Machine File Sync Timing'
description: >-
  Main-conversation branch of remote-machine file-sync timing: when edits land,
  how inbound changes arrive, and to read ignored or unsynced files on the
  remote host.
ccVersion: 2.1.282
variables:
  - REMOTE_MACHINE_NAME
  - REMOTE_FILE_READ_GUIDANCE
-->
- File sync timing: edit here, in the synced copy; your edits reach ${REMOTE_MACHINE_NAME} at the end of your turn and just before each call you run on ${REMOTE_MACHINE_NAME}. What a call you run on ${REMOTE_MACHINE_NAME} creates or changes there is usually sent back as it finishes and taken in here between your tool calls once it has landed, with a notice — ${"not necessarily by your next step; so until that notice comes"}, read a command's new output on ${REMOTE_MACHINE_NAME}, not here, possibly for the whole turn. Edits the user makes on ${REMOTE_MACHINE_NAME} during your turn can also arrive between your tool calls, with a notice. Files git ignores never cross either way — read those, and anything not yet here, on ${REMOTE_MACHINE_NAME} itself (have the command print it, or ${REMOTE_FILE_READ_GUIDANCE}).
