<!--
name: 'Data: Artifact Unobserved Connector Warning'
description: >-
  Publish warning that a declared connector/interface was never observed
  in-session.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1
  - DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2
-->
This page declares ${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_0(DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_1)} "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" but no successful call to it was observed in this session, so the page is published against an unobserved interface. Check the page's argument names against each tool's input schema if this session has the tool. The result fields the page reads stay unverified unless you can safely make one real call; otherwise tell the user the page's "${DATA_ARTIFACT_UNOBSERVED_CONNECTOR_WARNING_VAR_2}" integration is unverified.
