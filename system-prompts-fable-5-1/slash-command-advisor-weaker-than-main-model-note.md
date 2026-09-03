<!--
name: 'Slash Command: /advisor — advisor weaker than the main model'
description: >-
  Warns the model the chosen advisor is less capable than the main model so it
  will never activate, and names the two ways out, which is a recovery step the
  model can relay.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_ADVISOR_WEAKER_THAN_MAIN_MODEL_NOTE_VAR_0
  - SLASH_COMMAND_ADVISOR_WEAKER_THAN_MAIN_MODEL_NOTE_VAR_1
-->

Note: ${SLASH_COMMAND_ADVISOR_WEAKER_THAN_MAIN_MODEL_NOTE_VAR_0} is less capable than the current main model (${SLASH_COMMAND_ADVISOR_WEAKER_THAN_MAIN_MODEL_NOTE_VAR_1}), so the advisor will not activate. Choose a more capable advisor, or switch to a smaller main model.
