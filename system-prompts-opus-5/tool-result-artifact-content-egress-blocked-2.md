<!--
name: 'Tool Result: Artifact content egress blocked'
description: >-
  Reports that the environment's network allowlist blocked the artifact frame
  host so the artifact's content could not be fetched, and names the domain to
  allow
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0}, so the artifact's content cannot be fetched (your access to the artifact itself is fine — the permission check passed). ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_1}
