<!--
name: 'Slash Command: /model restricted by organization'
description: >-
  Result text when the requested model is restricted by the organization's
  settings, suggesting the model picker command or switching to a different
  model.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_0
  - SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_1
-->
Model '${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_0}' is restricted by your organization's settings. ${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_1?`Run ${SLASH_COMMAND_MODEL_RESTRICTED_BY_ORGANIZATION_VAR_1} to choose a different model.`:"Switch to a different model."}
