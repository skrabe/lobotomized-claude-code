<!--
name: Artifact copy_from Requires URL
description: >-
  validateInput error when copy_from omits url or from_url, naming which side's
  claude.ai URL is required.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_COPY_FROM_REQUIRES_URL_VAR_0
-->
action "copy_from" requires \`${TOOL_RESULT_ARTIFACT_COPY_FROM_REQUIRES_URL_VAR_0}\` — the ${TOOL_RESULT_ARTIFACT_COPY_FROM_REQUIRES_URL_VAR_0==="url"?"DESTINATION":"SOURCE"} Artifact's claude.ai URL (find it with action: "list").
