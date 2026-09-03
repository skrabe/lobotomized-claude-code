<!--
name: 'Tool Result: Artifact login blocked by credential source'
description: >-
  Artifact tool error returned when the session authenticates with a credential
  (API key, apiKeyHelper, OAuth token) that outranks a claude.ai account,
  telling the model how to get the user to re-login.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_0
  - TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_1
-->
Artifacts need a claude.ai login, and this session is authenticating with ${TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_0}, which takes precedence over a claude.ai account. ${TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_1} Then run /login and select "Claude account with subscription".
