<!--
name: Design consent not-granted retry error
description: >-
  Design MCP tool error returned to the model when consent is ungranted, telling
  it to ask the user to retry.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_CONSENT_NOT_GRANTED_RETRY_2_VAR_0
  - TOOL_RESULT_DESIGN_CONSENT_NOT_GRANTED_RETRY_2_VAR_1
-->
${TOOL_RESULT_DESIGN_CONSENT_NOT_GRANTED_RETRY_2_VAR_0.consentPromptFor(TOOL_RESULT_DESIGN_CONSENT_NOT_GRANTED_RETRY_2_VAR_1)} The user hasn't granted this yet — ask them to retry (the prompt will show on the next call) or run /design consent.
