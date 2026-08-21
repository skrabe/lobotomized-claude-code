<!--
name: 'Tool Result: Artifact Content Egress Blocked'
description: How to allowlist the artifact frame domain after a 403 egress-blocked read.
ccVersion: 2.1.238
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0
-->
To allow direct artifact reads here, add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0} to the environment's allowed domains: environment settings → Code → Network access → Custom → Allowed domains. An admin can add the same entry to a shared environment from admin settings → Cloud environments; sessions that run in that environment get the access.
