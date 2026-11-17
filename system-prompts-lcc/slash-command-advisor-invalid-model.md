<!--
name: /advisor invalid model
description: >-
  Told the model when the requested advisor model isn't allowed, listing the
  options.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_ADVISOR_INVALID_MODEL_VAR_0
  - SLASH_COMMAND_ADVISOR_INVALID_MODEL_VAR_1
-->
${SLASH_COMMAND_ADVISOR_INVALID_MODEL_VAR_0} can't be used as an advisor. Options: ${[...SLASH_COMMAND_ADVISOR_INVALID_MODEL_VAR_1(),"off"].join(", ")}
