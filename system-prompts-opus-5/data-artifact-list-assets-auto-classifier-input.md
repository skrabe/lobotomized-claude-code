<!--
name: Artifact list_assets classifier input
description: >-
  Auto-permission classifier input line for listing an artifact's assets, noting
  the conversation-wide read approval it carries.
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_LIST_ASSETS_AUTO_CLASSIFIER_INPUT_VAR_0
  - DATA_ARTIFACT_LIST_ASSETS_AUTO_CLASSIFIER_INPUT_VAR_1
-->
list an artifact's assets (read-only; a first approval also covers reading this artifact's assets and published files for the rest of the conversation)${DATA_ARTIFACT_LIST_ASSETS_AUTO_CLASSIFIER_INPUT_VAR_0} → ${DATA_ARTIFACT_LIST_ASSETS_AUTO_CLASSIFIER_INPUT_VAR_1}
