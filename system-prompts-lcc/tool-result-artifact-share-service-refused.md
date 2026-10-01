<!--
name: 'Artifact Share: Service Refused'
description: >-
  Artifact share tool error for HTTP 400/409/422: the artifact service refused
  the sharing change or read, with its detail or status; nothing changed.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_1
  - TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_2
-->
The artifact service refused this ${TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_0==="write"?"sharing change":"read"}${TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_1?`: ${TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_1}`:` (HTTP ${TOOL_RESULT_ARTIFACT_SHARE_SERVICE_REFUSED_VAR_2.status})`}. Nothing was changed.
