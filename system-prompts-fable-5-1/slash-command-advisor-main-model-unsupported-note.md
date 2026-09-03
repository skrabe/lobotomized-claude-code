<!--
name: 'Slash Command: /advisor — main model does not support the advisor'
description: >-
  Warns the model that the advisor it was just told about will not actually fire
  under the current main model, so it should not plan around advisor output.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADVISOR_MAIN_MODEL_UNSUPPORTED_NOTE_VAR_0
-->

Note: the current main model (${SLASH_COMMAND_ADVISOR_MAIN_MODEL_UNSUPPORTED_NOTE_VAR_0}) does not support the advisor. It will activate when you switch to a supported main model.
