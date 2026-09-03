<!--
name: Artifact Content Host Blocked Session
description: >-
  Publish/watch remedy when this session cannot read or hand over live artifact
  content because the content host is blocked.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_HOST_BLOCKED_SESSION_VAR_0
  - TOOL_RESULT_ARTIFACT_CONTENT_HOST_BLOCKED_SESSION_VAR_1
-->
The artifact content host is blocked from this session, so the live version can be neither read nor handed over here. ${TOOL_RESULT_ARTIFACT_CONTENT_HOST_BLOCKED_SESSION_VAR_0(TOOL_RESULT_ARTIFACT_CONTENT_HOST_BLOCKED_SESSION_VAR_1)} Tell the user, and publish again only once you can build on the live version.
