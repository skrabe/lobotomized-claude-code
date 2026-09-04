<!--
name: 'System Reminder: Remote machine file sync timing for subagents'
description: >-
  Explains outbound file sync before remote calls and delayed inbound
  reconciliation by the main conversation, directing subagents to read fresh or
  ignored files on the remote machine
ccVersion: 2.1.261
variables:
  - REMOTE_MACHINE_NAME
  - REMOTE_FILE_READ_GUIDANCE
-->
- File sync timing: edit here, in the synced copy; your edits reach ${REMOTE_MACHINE_NAME} just before each call you run on ${REMOTE_MACHINE_NAME}, and otherwise when the conversation's turn ends. What a call you run on ${REMOTE_MACHINE_NAME} creates or changes there is sent back as it finishes, but this task does not take it in: the main conversation writes it into this session's copy (once this task hands back — or, if the main conversation is still running beside this task, at its next step; the "Directory sync:" line under the result says so) — so within this task, read a command's new output on ${REMOTE_MACHINE_NAME} itself. If ${REMOTE_MACHINE_NAME} cannot send it now, you are told so and what to expect. Edits the user makes on ${REMOTE_MACHINE_NAME} meanwhile reach this copy the same way — at the main conversation's steps, not yours, and with no notice to you. Files git ignores never cross either way — read those, and anything not yet here, on ${REMOTE_MACHINE_NAME} (have the command print it, or ${REMOTE_FILE_READ_GUIDANCE}).
