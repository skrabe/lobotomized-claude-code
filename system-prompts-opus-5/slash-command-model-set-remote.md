<!--
name: 'Slash Command: /model — model switched in a cloud session'
description: >-
  Confirms to the model which model the remote/cloud session was switched to,
  the sibling branch of the workspace-default reset notice.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MODEL_SET_REMOTE_VAR_0
  - SLASH_COMMAND_MODEL_SET_REMOTE_VAR_1
  - SLASH_COMMAND_MODEL_SET_REMOTE_VAR_2
-->
Set model to ${SLASH_COMMAND_MODEL_SET_REMOTE_VAR_0.bold(SLASH_COMMAND_MODEL_SET_REMOTE_VAR_1(SLASH_COMMAND_MODEL_SET_REMOTE_VAR_2))}
