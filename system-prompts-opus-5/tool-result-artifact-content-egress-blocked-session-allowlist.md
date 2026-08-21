<!--
name: 'Tool Result: Artifact Content Egress Blocked Session Allowlist'
description: >-
  Allowlist remediation interpolated into the artifact-read egress-blocked tool
  error for local/sandbox sessions.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_SESSION_ALLOWLIST_VAR_0
-->
To allow artifact reads here, add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_SESSION_ALLOWLIST_VAR_0} to the network allowlist this session runs behind — the sandbox's allowed domains, or the Claude desktop app's network settings (Settings → Capabilities; a workspace admin can add it on Team/Enterprise).
