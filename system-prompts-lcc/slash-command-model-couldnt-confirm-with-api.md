<!--
name: 'Slash Command: /model — Couldn''t Confirm Model With API'
description: >-
  Tells the model the /model server probe could not confirm the requested model
  (no answer, or the account changed mid-probe), so it was not applied. It
  includes a retry or list-models hint.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_0
  - SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_1
  - SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_2
-->
Couldn't confirm model "${SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_0(SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_1)}" with the API. ${SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_2?`Try again, or run ${SLASH_COMMAND_MODEL_COULDNT_CONFIRM_WITH_API_VAR_2} to see available models.`:"Try again."}
