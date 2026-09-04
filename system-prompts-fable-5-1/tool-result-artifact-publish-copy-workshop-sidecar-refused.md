<!--
name: Artifact Publish Copy Workshop Sidecar Refused
description: >-
  Tool result when a workshop page would ship copied renderable or executable
  sidecar files.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_2
-->
workshop pages cannot ship renderable or executable sidecar files — each is a URL that bypasses the publish-time verifier: ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_1.join(", "))} (copied). Nothing was published.${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_WORKSHOP_SIDECAR_REFUSED_VAR_2}
