<!--
name: 'Slash Command: /advisor model consent required'
description: >-
  /advisor message when the chosen advisor model needs consent first: tells the
  user to run the model command (in an interactive terminal session when needed)
  to review and enable it, then set it as advisor.
ccVersion: 2.1.292
variables:
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_0
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_1
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_2
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_3
-->
${SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_0(SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_1)} Run ${SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_2(SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_1)}${SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_3?" in an interactive terminal session":""} to review and enable, then set it as the advisor.
