<!--
name: 'Tool Result: Sandbox SigV4 body too large to re-sign'
description: >-
  Sandbox proxy denial text when a masked-credential SigV4 request signs a
  literal body hash whose body exceeds the buffering limit, suggesting
  UNSIGNED-PAYLOAD or an unmasked credential.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_BASH_SANDBOX_SIGV4_BODY_TOO_LARGE_TO_RESIGN_VAR_0
-->

AWS SigV4 request uses a masked credential and signs a literal body hash, so the proxy must buffer the body to re-sign it, but the body exceeds the ${TOOL_RESULT_BASH_SANDBOX_SIGV4_BODY_TOO_LARGE_TO_RESIGN_VAR_0}-byte buffering limit; denied. Sign the payload as UNSIGNED-PAYLOAD to stream it without buffering, or use an unmasked credential to have the request forwarded untouched.
