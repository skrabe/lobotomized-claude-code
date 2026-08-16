<!--
name: 'Slash Command: /plugin validate — validation crashed'
description: >-
  Distinguishes a crash of the validator itself from a manifest that failed
  validation, so the model does not report the plugin as invalid when the run
  never completed.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_1
  - SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_2
  - SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_3
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_0.cross} Unexpected error during validation: ${SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_1(SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_2(SLASH_COMMAND_PLUGIN_VALIDATE_UNEXPECTED_ERROR_VAR_3),200)}
