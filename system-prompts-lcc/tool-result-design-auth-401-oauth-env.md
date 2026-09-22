<!--
name: Design Auth 401 OAuth Env Token
description: >-
  Auth-failure message for a CLAUDE_CODE_OAUTH_TOKEN env-var token with no
  refresh, advising `claude setup-token`; returned to the model as a
  ClaudeDesign tool_result error.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_DESIGN_AUTH_401_OAUTH_ENV_VAR_0
  - TOOL_RESULT_DESIGN_AUTH_401_OAUTH_ENV_VAR_1
-->
${TOOL_RESULT_DESIGN_AUTH_401_OAUTH_ENV_VAR_0} This session authenticates with the CLAUDE_CODE_OAUTH_TOKEN environment variable, which has no refresh token — it cannot self-heal and has likely expired or been revoked. Mint a fresh token with \`claude setup-token\` and restart the session with it${TOOL_RESULT_DESIGN_AUTH_401_OAUTH_ENV_VAR_1?"":", or unset it and run /login"}.
