<!--
name: Design Auth 401 Remote Session
description: >-
  Auth-failure message for a remote session whose credential is
  host-injected/self-healing; returned to the model as a ClaudeDesign
  tool_result error.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_DESIGN_AUTH_401_REMOTE_SESSION_VAR_0
-->
${TOOL_RESULT_DESIGN_AUTH_401_REMOTE_SESSION_VAR_0} This remote session's credential is injected and rotated by the session host — it usually self-heals within minutes. Retry shortly; if this persists, the host session needs attention.
