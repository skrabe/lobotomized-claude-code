<!--
name: 'Tool result: Bash sandbox SigV4 STS/IAM not signed'
description: >-
  Sandbox proxy denial: only GetCallerIdentity is signed for STS/IAM unless the
  host is added to injectHosts
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_BASH_SANDBOX_SIGV4_STS_IAM_HOST_NOT_INJECTED_VAR_0
  - TOOL_RESULT_BASH_SANDBOX_SIGV4_STS_IAM_HOST_NOT_INJECTED_VAR_1
-->
For AWS STS and IAM the sandbox signs only GetCallerIdentity, because other calls can return credentials it cannot mask. To allow them, the user adds the STS or IAM host by name (this request went to "${TOOL_RESULT_BASH_SANDBOX_SIGV4_STS_IAM_HOST_NOT_INJECTED_VAR_0}") to injectHosts of the ${TOOL_RESULT_BASH_SANDBOX_SIGV4_STS_IAM_HOST_NOT_INJECTED_VAR_1.accessKeyIdVar} entry in their user settings, beside the other hosts that key needs.
