<!--
name: 'Data: Artifact Gateway Temporarily Unable'
description: >-
  Gateway-relay why string for HTTP unavailable after one retry, interpolated
  into artifact-read errors as ${ce.why}.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_GATEWAY_TEMPORARILY_UNABLE_VAR_0
-->
temporarily unable: HTTP ${DATA_ARTIFACT_GATEWAY_TEMPORARILY_UNABLE_VAR_0.status} after one retry, so a later read may succeed
