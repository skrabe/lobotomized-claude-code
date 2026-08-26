<!--
name: 'Tool Result: Memory Write Content Secrets Blocked'
description: >-
  Refused memory-write tool result when scanned content looks like credentials
  and must not be stored, including in shared project stores.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_MEMORY_WRITE_CONTENT_SECRETS_BLOCKED_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_CONTENT_SECRETS_BLOCKED_VAR_1
-->
Content contains potential secrets (${TOOL_RESULT_MEMORY_WRITE_CONTENT_SECRETS_BLOCKED_VAR_0.map((TOOL_RESULT_MEMORY_WRITE_CONTENT_SECRETS_BLOCKED_VAR_1)=>TOOL_RESULT_MEMORY_WRITE_CONTENT_SECRETS_BLOCKED_VAR_1.label).join(", ")}) and cannot be written to memory. Memory stores are never a place for credentials, and project stores are shared with every collaborator. Remove the sensitive content and try again.
