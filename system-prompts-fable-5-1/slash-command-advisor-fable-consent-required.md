<!--
name: Advisor Fable Consent Required
description: >-
  /advisor local-jsx onDone and type:local stdout telling the user to enable
  Fable via /model before setting it as advisor.
ccVersion: 2.1.261
variables:
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_0
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_1
  - SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_2
-->
${SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_0(SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_1)} Run /model fable${SLASH_COMMAND_ADVISOR_FABLE_CONSENT_REQUIRED_VAR_2?" in an interactive terminal session":""} to review and enable, then set it as the advisor.
