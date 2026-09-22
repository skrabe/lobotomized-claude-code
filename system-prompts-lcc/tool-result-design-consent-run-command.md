<!--
name: Design consent run-command error
description: >-
  Design MCP tool error returned to the model when consent must be granted via
  /design consent in this permission mode.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_CONSENT_RUN_COMMAND_VAR_0
  - TOOL_RESULT_DESIGN_CONSENT_RUN_COMMAND_VAR_1
-->
${TOOL_RESULT_DESIGN_CONSENT_RUN_COMMAND_VAR_0.consentPromptFor(TOOL_RESULT_DESIGN_CONSENT_RUN_COMMAND_VAR_1)} The user hasn't granted this — run /design consent to grant it (it can't be approved automatically in this permission mode).
