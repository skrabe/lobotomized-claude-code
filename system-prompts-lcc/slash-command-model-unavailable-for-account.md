<!--
name: 'Slash command: model unavailable for account'
description: >-
  /model message that the requested model is disabled for this account, followed
  by its description.
ccVersion: 2.1.316
variables:
  - SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_0
  - SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_1
  - SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_2
  - SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_3
-->
Model '${SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_0(SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_1)}' is not currently available for your account. ${SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_2(SLASH_COMMAND_MODEL_UNAVAILABLE_FOR_ACCOUNT_VAR_3.description)}
