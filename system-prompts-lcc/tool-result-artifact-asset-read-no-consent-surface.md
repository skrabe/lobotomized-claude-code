<!--
name: Artifact read/list — no consent surface for another person's artifact
description: >-
  Deny message when a first read or listing of a non-owned (or co-written)
  artifact's files/assets needs a consent surface that this session cannot show;
  tells the model to raise the read in chat and not retry.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_READ_NO_CONSENT_SURFACE_VAR_0
-->
Reading or listing ${TOOL_RESULT_ARTIFACT_ASSET_READ_NO_CONSENT_SURFACE_VAR_0} needs a consent surface, and no one can answer the prompt in this session — raise the read with the user in chat; do not retry it in this session.
