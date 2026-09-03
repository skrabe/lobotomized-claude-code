<!--
name: Artifact Unobserved Connector Warning
description: >-
  Warning appended to the artifact-read/publish tool result telling the model a
  declared connector had no observed call, directing it to verify or tell the
  user; injected into the model's context via the warnings array.
ccVersion: 2.1.238
variables:
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2
-->
This page declares ${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0(DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1)} "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" but no successful call to it was observed in this session, so the page is published against an unobserved interface. Verify its calls against a real response if you can safely make one, or tell the user the page's "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" integration is unverified.
