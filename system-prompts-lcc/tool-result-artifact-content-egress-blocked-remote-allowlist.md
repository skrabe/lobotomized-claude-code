<!--
name: 'Tool Result: Artifact Content Egress Blocked Remote Allowlist'
description: >-
  Allowlist remediation interpolated into the artifact-read egress-blocked tool
  error for CLAUDE_CODE_REMOTE sessions.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_REMOTE_ALLOWLIST_VAR_0
-->
To allow artifact reads here, add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_REMOTE_ALLOWLIST_VAR_0} to the network allowlist of the environment this remote session runs in.
