<!--
name: Safety-judge user identity rule
description: >-
  Injected rule for the safety judge resolving $USER and flagging other-user
  branches.
ccVersion: 2.1.206
variables:
  - AGENT_PROMPT_PERMISSION_JUDGE_USER_IDENTITY_VAR_0
-->
**User identity**: \`${AGENT_PROMPT_PERMISSION_JUDGE_USER_IDENTITY_VAR_0}\`. The \`$USER/...\` pattern in the rules above resolves to \`${AGENT_PROMPT_PERMISSION_JUDGE_USER_IDENTITY_VAR_0}/...\`. Branches whose first path segment is a different person's name (\`<other-user>/...\`) are NOT this user's personal branches.
