<!--
name: Artifact List-By-Type Auto-Classifier Input
description: >-
  toAutoClassifierInput string for listing Artifacts made from a type, including
  the non-mine titles-and-descriptions note.
ccVersion: 2.1.257
variables:
  - DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_0
  - DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_1
  - DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_2
-->
list artifacts made from a type (read-only, scope: ${DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_0}${DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_0==="mine"?"":" — includes titles and descriptions of artifacts other users in the organization published"}): ${DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_1(DATA_ARTIFACT_LIST_BY_TYPE_AUTO_CLASSIFIER_INPUT_VAR_2)}
