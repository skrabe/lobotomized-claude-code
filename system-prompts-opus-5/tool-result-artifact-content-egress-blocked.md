<!--
name: 'Tool Result: Artifact content egress blocked'
description: >-
  Reports that the environment's network allowlist blocked the artifact frame
  host so the artifact's content could not be fetched, and names the domain to
  allow
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0}, so the artifact's content cannot be fetched (your access to the artifact itself is fine — the permission check passed). To allow artifact reads here, add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_1} to the environment's allowed domains: environment settings → Code → Network access → Custom → Allowed domains. An admin can add the same entry to a shared environment from admin settings → Cloud environments; sessions that run in that environment get the access.
