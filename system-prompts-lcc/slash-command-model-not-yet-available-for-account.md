<!--
name: 'Slash Command: /model not yet available for account'
description: >-
  Result text when a model (e.g. Fable) is not yet available for the user's
  account, suggesting the model picker command or switching to a different
  model.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_NOT_YET_AVAILABLE_FOR_ACCOUNT_VAR_0
  - SLASH_COMMAND_MODEL_NOT_YET_AVAILABLE_FOR_ACCOUNT_VAR_1
-->
${SLASH_COMMAND_MODEL_NOT_YET_AVAILABLE_FOR_ACCOUNT_VAR_0.displayName} isn't available for your account yet. ${SLASH_COMMAND_MODEL_NOT_YET_AVAILABLE_FOR_ACCOUNT_VAR_1?`Run ${SLASH_COMMAND_MODEL_NOT_YET_AVAILABLE_FOR_ACCOUNT_VAR_1} to pick another model.`:"Switch to a different model."}
