<!--
name: Artifact verify Auto-Classifier Input
description: >-
  toAutoClassifierInput line describing a pending verify diagnostics read,
  including the unattended-notification clause when that applies.
ccVersion: 2.1.238
variables:
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_0
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_1
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_2
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_3
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_4
  - DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_5
-->
read an artifact's runtime diagnostics (read-only; console output and errors captured from viewers' browsers${DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_0!==null&&DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_1(DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_0.slug)?"; requested after an unattended auto-reply notification — diagnostics are captured from artifact viewers":""})${DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_2(DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_3)}${DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_4(DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_3)} → ${DATA_ARTIFACT_VERIFY_AUTO_CLASSIFIER_INPUT_VAR_5}
