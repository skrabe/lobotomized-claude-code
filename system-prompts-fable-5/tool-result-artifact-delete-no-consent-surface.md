<!--
name: Artifact delete — no confirmation surface
description: >-
  Deny message when an Artifact delete needs the user's confirmation but no one
  can answer it in this session.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_NO_CONSENT_SURFACE_VAR_0
-->
Deleting an Artifact needs the user's confirmation, and no one can answer it in this session, so nothing was deleted. Do not retry the delete in this session; ${TOOL_RESULT_ARTIFACT_DELETE_NO_CONSENT_SURFACE_VAR_0(TOOL_RESULT_ARTIFACT_DELETE_NO_CONSENT_SURFACE_VAR_1())}
