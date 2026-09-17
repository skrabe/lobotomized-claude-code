<!--
name: Artifact Quickstart Auto-Classifier Input
description: >-
  toAutoClassifierInput line for quickstart listing published Artifact types and
  design systems the user can open.
ccVersion: 2.1.274
variables:
  - DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0
  - DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_1
-->
quickstart (read-only, intent: ${DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0}): lists the published Artifact types and the design systems this user can open — titles and descriptions other people in the organization wrote${DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0==="slides"||DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0==="design"?` — and reads the README of the account's default design system, if there is one, skipped where that read would need approval${!DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_1?"":"; where that system's published files, and the matched type's, can be saved to the session's scratchpad, they are listed instead of the README, each skipped where reading it would need approval"}`:""}
