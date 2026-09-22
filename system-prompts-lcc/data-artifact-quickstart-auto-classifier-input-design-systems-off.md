<!--
name: Artifact Quickstart Auto-Classifier Input (Design Systems Off)
description: >-
  toAutoClassifierInput line for quickstart when design systems are left out,
  summarizing a types-only listing.
ccVersion: 2.1.274
variables:
  - DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_0
  - DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_1
-->
quickstart (read-only, intent: ${DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_0}, design systems left out): lists the published Artifact types — titles and descriptions their publishers wrote${!DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_1||DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_0!=="slides"&&DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_DESIGN_SYSTEMS_OFF_VAR_0!=="design"?"":"; where they can be, the matched type's published files are saved to the session's scratchpad and listed, skipped where reading them would need approval"}
