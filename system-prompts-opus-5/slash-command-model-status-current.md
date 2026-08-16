<!--
name: 'Slash Command: /model — current model status line'
description: >-
  States which model is running right now, with the previous model and effort
  appended, so the model can answer accurately about its own identity and
  configuration.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_0
  - SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_1
  - SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_2
-->
Current model: ${SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_0}${SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_1}${SLASH_COMMAND_MODEL_STATUS_CURRENT_VAR_2}
