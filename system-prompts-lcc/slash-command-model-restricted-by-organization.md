<!--
name: 'Slash command: model restricted by organization'
description: >-
  /model message that the requested model is restricted by organization
  settings, with a hint to choose another.
ccVersion: 2.1.316
variables:
  - SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_0
  - SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_1
  - SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_2
-->
Model '${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_0(SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_1)}' is restricted by your organization's settings. ${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_2?`Run ${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_2} to choose a different model.`:"Switch to a different model."}
