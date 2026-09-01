<!--
name: Design login missing scopes
description: >-
  DesignSync precondition tool-error shown to the model when the auth server did
  not grant design scopes.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_LOGIN_MISSING_SCOPES_VAR_0
-->
The authorization server did not grant the design scopes (missing: ${TOOL_RESULT_DESIGN_LOGIN_MISSING_SCOPES_VAR_0.join(", ")}) — the Claude Design app registration may be incomplete or out of date.
