<!--
name: 'Slash Command: /advisor — model rejected, valid options listed'
description: >-
  Tells the model the requested advisor was rejected and enumerates the accepted
  values, so it can suggest a valid one instead of retrying the same name.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADVISOR_INVALID_MODEL_OPTIONS_VAR_0
  - SLASH_COMMAND_ADVISOR_INVALID_MODEL_OPTIONS_VAR_1
-->
${SLASH_COMMAND_ADVISOR_INVALID_MODEL_OPTIONS_VAR_0} cannot be used as an advisor. Valid options: ${[...SLASH_COMMAND_ADVISOR_INVALID_MODEL_OPTIONS_VAR_1(),"off"].join(", ")}
