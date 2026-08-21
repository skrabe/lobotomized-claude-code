<!--
name: 'Data: Artifact Unobserved Connector Warning'
description: >-
  Publish warning that a declared connector/interface was never observed
  in-session.
ccVersion: 2.1.238
variables:
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2
-->
This page declares ${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0(DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1)} "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" but no successful call to it was observed in this session, so the page is published against an unobserved interface. Verify its calls against a real response if you can safely make one, or tell the user the page's "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" integration is unverified.
