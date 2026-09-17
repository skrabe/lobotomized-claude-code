<!--
name: 'Tool Result: Artifact Login Blocked By Credential'
description: >-
  Explains that Artifact calls are blocked because a non-claude.ai credential
  takes precedence and tells the model how to get a subscription login.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_0
  - TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_1
  - TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_2
-->
${TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_0}, and this session is authenticating with ${TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_1}, which takes precedence over a claude.ai account. ${TOOL_RESULT_ARTIFACT_LOGIN_BLOCKED_BY_CREDENTIAL_VAR_2} Then run /login and select "Claude account with subscription".
