<!--
name: 'Tool Result: Artifact Content Egress Blocked For Tokenless Public Artifact'
description: >-
  Artifact-read error when the allowlist blocks the frame host and public
  tokenless artifacts are not served through the session gateway, so content
  cannot be fetched.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_TOKENLESS_VAR_0
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_TOKENLESS_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_TOKENLESS_VAR_0}, and public (tokenless) artifacts are not served through the session gateway, so the artifact's content cannot be fetched (your access to the artifact itself is fine — the permission check passed). ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_TOKENLESS_VAR_1}
