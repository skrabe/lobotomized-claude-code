<!--
name: Artifact Content Egress Blocked Cowork Allow Network
description: >-
  Cowork cloud-session network-egress remedy interpolated into artifact
  read/publish tool results when the content host is blocked.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_COWORK_ALLOW_NETWORK_VAR_0
-->
This cloud session's network access follows the "Allow network egress" setting for Cowork in claude.ai, not an environment allowlist. To allow direct artifact reads here, an organization admin (or the user, on an individual plan) can turn that setting on and either allow all domains or add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_COWORK_ALLOW_NETWORK_VAR_0} to its additional allowed domains.
