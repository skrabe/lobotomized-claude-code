<!--
name: 'Tool Result: Artifact Content Egress Blocked'
description: >-
  Allowlist remediation appended to an artifact-content fetch error when the
  environment blocked the frame host.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0
-->
To allow direct artifact reads here, add ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_VAR_0.env==="staging"?"*.frame.staging.claudeusercontent.com":"*.frame.claudeusercontent.com"} to the environment's allowed domains: environment settings → Code → Network access → Custom → Allowed domains. An admin can add the same entry to a shared environment from admin settings → Cloud environments; sessions that run in that environment get the access.
