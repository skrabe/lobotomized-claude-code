<!--
name: Artifact asset egress blocked
description: >-
  Reworded 2.1.224 version of the dropped 2.1.221 id (added the 'not reachable
  through this environment's network allowlist' clause) — the Artifact/WebFetch
  asset-read error handed back to the model when the egress proxy blocks the
  artifact frame host.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_EGRESS_BLOCKED_VAR_0
-->
the network egress proxy in this environment blocks ${TOOL_RESULT_ARTIFACT_ASSET_EGRESS_BLOCKED_VAR_0} — not reachable through this environment's network allowlist; your access to the artifact itself is fine (the boot check passed)
