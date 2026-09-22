<!--
name: 'Tool Result: Artifact login required (remote session)'
description: >-
  Artifact tool validation/call error returned to the model when the remote
  session's launching machine is not signed in to claude.ai.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_LOGIN_REQUIRED_REMOTE_SESSION_VAR_0
-->
${TOOL_RESULT_ARTIFACT_LOGIN_REQUIRED_REMOTE_SESSION_VAR_0}, and this remote session authenticates through the machine that launched it, which is not signed in to claude.ai. Sign in to claude.ai on that machine (/login, "Claude account with subscription"), then reconnect this session.
