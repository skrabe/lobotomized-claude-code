<!--
name: 'Tool Result: Memory Write Blocked (Secrets)'
description: >-
  memory-write tool_result blocking content with potential secrets from personal
  memory; tells the model to remove sensitive content and retry.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_MEMORY_WRITE_SECRETS_BLOCKED_VAR_0
-->
Content contains potential secrets (${TOOL_DESCRIPTION_MEMORY_WRITE_SECRETS_BLOCKED_VAR_0}) and cannot be written to memory. Remove the sensitive content and try again.
