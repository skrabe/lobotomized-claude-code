<!--
name: 'System Reminder: Attached machine untrusted attachments refusal'
description: >-
  Tells the agent a call to an attached machine was refused because the session
  has repositories or files attached that its owner has not marked trusted, that
  retrying or reconnecting will not help, and how the person can clear or work
  around the block
ccVersion: 2.1.291
variables:
  - REMOTE_MACHINE_NAME
  - LIST_COMPUTER_FOLDERS_TOOL_NAME
  - REQUEST_COMPUTER_FOLDER_TOOL_NAME
-->
This session has repositories or files attached that its owner has not said they trust, so its calls to ${REMOTE_MACHINE_NAME} are not accepted. Nothing was done for this one. Sending the same call again will not change that. Call ${LIST_COMPUTER_FOLDERS_TOOL_NAME} once. If it refuses with a trust question, put the question to the person: their yes clears this. If it lists folders, call ${REQUEST_COMPUTER_FOLDER_TOOL_NAME} for the folder this session was using: the person's Allow clears this. If neither asks the person anything, or ${REMOTE_MACHINE_NAME} still refuses after their answer, tell them plainly what stays blocked, and that a new session with no repository and none of their files can run a quick command.
