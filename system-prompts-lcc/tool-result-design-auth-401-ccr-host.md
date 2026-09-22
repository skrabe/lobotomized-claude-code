<!--
name: Design Auth 401 CCR Host Token
description: >-
  Auth-failure message for a CCR-host-injected OAuth token with no refresh
  token; returned to the model as a ClaudeDesign tool_result error.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_DESIGN_AUTH_401_CCR_HOST_VAR_0
-->
${TOOL_RESULT_DESIGN_AUTH_401_CCR_HOST_VAR_0} This session authenticates with an OAuth token injected by the CCR host, which has no refresh token — it cannot self-heal and has likely expired or been revoked. The credential comes from the host session; check or restart it there.
