<!--
name: 'Tool Result: Artifact asset read blocked by network allowlist'
description: >-
  Artifact read_asset failure explaining the environment's network allowlist
  blocks the frame host so the asset cannot be fetched, and which domain to
  allow
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_READ_EGRESS_BLOCKED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_READ_EGRESS_BLOCKED_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_ASSET_READ_EGRESS_BLOCKED_VAR_0}, so the asset cannot be fetched (access to the artifact itself is fine). To allow it, add *.${TOOL_RESULT_ARTIFACT_ASSET_READ_EGRESS_BLOCKED_VAR_1} to the network allowlist this session runs behind (the sandbox's allowed domains, or the Claude desktop app's network settings).
