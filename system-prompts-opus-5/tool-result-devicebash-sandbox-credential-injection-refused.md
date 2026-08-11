<!--
name: 'Tool Result: Device Bash Sandbox Credential Injection Refused'
description: >-
  Returned to the model when device_bash is refused because sandbox credential
  masking could expose real credentials.
ccVersion: 2.1.227
variables:
  - TOOL_RESULT_DEVICEBASH_SANDBOX_CREDENTIAL_INJECTION_REFUSED_VAR_0
-->
${TOOL_RESULT_DEVICEBASH_SANDBOX_CREDENTIAL_INJECTION_REFUSED_VAR_0} refused: this device's sandbox is configured to inject real credentials into sandboxed network requests (sandbox.credentials entries with mode "mask"), which a remote command must not inherit. Remove or change those entries on the device to use device_bash.
