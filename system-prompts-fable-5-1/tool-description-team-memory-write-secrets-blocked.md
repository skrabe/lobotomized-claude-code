<!--
name: 'Tool Result: Team Memory Write Blocked (Secrets)'
description: >-
  team-memory-write tool_result blocking content with potential secrets; tells
  the model to remove sensitive content and retry.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_TEAM_MEMORY_WRITE_SECRETS_BLOCKED_VAR_0
-->
Content contains potential secrets (${TOOL_DESCRIPTION_TEAM_MEMORY_WRITE_SECRETS_BLOCKED_VAR_0}) and cannot be written to team memory, which is shared with all repository collaborators. Remove the sensitive content and try again.
