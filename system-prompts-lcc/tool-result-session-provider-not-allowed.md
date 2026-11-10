<!--
name: 'Tool Result: Session provider not allowed'
description: >-
  Error when a delegated session's requests would go to a gateway, custom
  endpoint or project provider setting instead of Anthropic's API or an allowed
  cloud provider
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_SESSION_PROVIDER_NOT_ALLOWED_VAR_0
-->
${TOOL_RESULT_SESSION_PROVIDER_NOT_ALLOWED_VAR_0}: its requests must go to Anthropic's API or a cloud provider this machine is set up for, so a gateway, a custom endpoint, or a project's provider, credential or model settings aren't allowed. Remove the setting, such as ANTHROPIC_BASE_URL, from wherever it's set, or ask whoever runs this machine to.
