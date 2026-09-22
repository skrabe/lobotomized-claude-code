<!--
name: 'Tool Result: Sandbox SigV4 masked-credential denial'
description: >-
  Sandbox proxy denial text for presigned/streaming/sigv4a AWS requests signed
  with a masked credential, explaining the credentials.sigv4 passthrough option;
  surfaces in sandboxed command output.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_BASH_SANDBOX_SIGV4_MASKED_CREDENTIAL_DENIED_VAR_0
-->

AWS SigV4 ${TOOL_RESULT_BASH_SANDBOX_SIGV4_MASKED_CREDENTIAL_DENIED_VAR_0.kind} request uses a masked credential but cannot be re-signed by the sandbox proxy; denied by policy. Set credentials.sigv4.${TOOL_RESULT_BASH_SANDBOX_SIGV4_MASKED_CREDENTIAL_DENIED_VAR_0.kind} to "passthrough" to forward it unmodified (it will fail upstream: the signature covers the masked placeholder).
