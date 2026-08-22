<!--
name: 'Tool result: Artifact content host egress blocked'
description: >-
  Publish/read remedy text saying the artifact content host is blocked by the
  allowlist, naming the domain and settings path, and telling the model to
  publish only once it can build on the live version
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_HOST_EGRESS_BLOCKED_VAR_0
-->
This environment's network allowlist blocks the artifact content host, so the live version can be neither read nor handed over here until ${TOOL_RESULT_ARTIFACT_CONTENT_HOST_EGRESS_BLOCKED_VAR_0==="staging"?"*.frame.staging.claudeusercontent.com":"*.frame.claudeusercontent.com"} is added at environment settings → Code → Network access → Custom → Allowed domains. An admin can add the same entry to a shared environment from admin settings → Cloud environments; sessions that run in that environment get the access. Tell the user, and publish again only once you can build on the live version.
