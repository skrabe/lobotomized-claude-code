<!--
name: Artifact Quickstart Auto-Classifier Input
description: >-
  toAutoClassifierInput line for quickstart listing published Artifact types and
  design systems the user can open.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0
-->
quickstart (read-only, intent: ${DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0}): lists the published Artifact types and the design systems this user can open — titles and descriptions other people in the organization wrote${DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0==="slides"||DATA_ARTIFACT_QUICKSTART_AUTO_CLASSIFIER_INPUT_VAR_0==="design"?" — and reads the README of the account's default design system, if there is one, skipped where that read would need approval":""}
