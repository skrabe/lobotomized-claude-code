<!--
name: Artifact Delete - Consent Surface Gone
description: >-
  Artifact delete error saying the session can no longer ask the user to
  confirm, so nothing was deleted and the delete must not be retried.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_CONSENT_SURFACE_GONE_VAR_0
-->
Deleting an Artifact needs the user's confirmation and this session no longer has a way to ask — nothing was deleted; do not retry the delete in this session. Instead, ${TOOL_RESULT_ARTIFACT_DELETE_CONSENT_SURFACE_GONE_VAR_0(TOOL_RESULT_ARTIFACT_DELETE_CONSENT_SURFACE_GONE_VAR_1())}
