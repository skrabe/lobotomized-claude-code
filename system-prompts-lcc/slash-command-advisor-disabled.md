<!--
name: 'Slash Command: /advisor — advisor turned off'
description: >-
  Tells the model no advisor model is in play any more, and whether the change
  is session-scoped, so it stops expecting reviewer-model iterations.
ccVersion: 2.1.276
variables:
  - SLASH_COMMAND_ADVISOR_DISABLED_VAR_0
  - SLASH_COMMAND_ADVISOR_DISABLED_VAR_1
  - SLASH_COMMAND_ADVISOR_DISABLED_VAR_2
  - SLASH_COMMAND_ADVISOR_DISABLED_VAR_3
-->
Advisor disabled${SLASH_COMMAND_ADVISOR_DISABLED_VAR_0}${SLASH_COMMAND_ADVISOR_DISABLED_VAR_1(SLASH_COMMAND_ADVISOR_DISABLED_VAR_2,void 0,SLASH_COMMAND_ADVISOR_DISABLED_VAR_3)}
