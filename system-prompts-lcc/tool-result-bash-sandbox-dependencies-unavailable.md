<!--
name: 'Tool Result: Bash sandbox dependencies unavailable'
description: >-
  Sandbox init error listing missing sandbox dependencies; surfaces via the
  required-sandbox init failure in the Bash tool result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_SANDBOX_DEPENDENCIES_UNAVAILABLE_VAR_0
-->
Sandbox dependencies not available: ${TOOL_RESULT_BASH_SANDBOX_DEPENDENCIES_UNAVAILABLE_VAR_0.errors.join(", ")}
