<!--
name: 'Slash Command: /model — model switched'
description: >-
  Tells the model which model is now in use and whether the change was saved as
  the new default or applies to this session only.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MODEL_SET_VAR_0
  - SLASH_COMMAND_MODEL_SET_VAR_1
  - SLASH_COMMAND_MODEL_SET_VAR_2
  - SLASH_COMMAND_MODEL_SET_VAR_3
-->
Set model to ${SLASH_COMMAND_MODEL_SET_VAR_0.bold(SLASH_COMMAND_MODEL_SET_VAR_1(SLASH_COMMAND_MODEL_SET_VAR_2))}${SLASH_COMMAND_MODEL_SET_VAR_3?" and saved as your default for new sessions":" for this session only"}
