<!--
name: 'Data: Artifact Attached — Current Artifact Of Interest'
description: >-
  Meta message injected into the conversation when the user attaches an artifact
  to the session, instructing Claude to re-read it (Artifact read_page_data with
  the workshop-decisions schema for workshop pages, otherwise WebFetch) before
  editing or republishing it.
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_0
  - DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_1
  - DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_2
-->
The user attached the artifact ${DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_0} to this session as the current artifact of interest. re-read it before editing or republishing (${DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_1()}).${DATA_ARTIFACT_ATTACHED_CURRENT_ARTIFACT_OF_INTEREST_VAR_2}
