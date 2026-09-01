<!--
name: Design Auth 401 Login Expired/Revoked
description: >-
  Auth-failure suffix telling the model the /design login credential is
  expired/revoked and how to re-authenticate; returned as a ClaudeDesign
  tool_result error.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_DESIGN_AUTH_401_LOGIN_EXPIRED_VAR_0
  - TOOL_RESULT_DESIGN_AUTH_401_LOGIN_EXPIRED_VAR_1
-->
${TOOL_RESULT_DESIGN_AUTH_401_LOGIN_EXPIRED_VAR_0} The design credential (from /design login) is expired or revoked${TOOL_RESULT_DESIGN_AUTH_401_LOGIN_EXPIRED_VAR_1?", and /design login requires an interactive terminal — re-authenticate outside this session":" — run /design login to re-authenticate"}.
