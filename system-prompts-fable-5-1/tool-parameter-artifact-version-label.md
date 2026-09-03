<!--
name: Artifact version label parameter
description: >-
  Model-facing Artifact tool `label` input-schema param description (short
  human-readable version name shown in the version picker). 2.1.193 reworded the
  opening (fuzzy-miss restore).
ccVersion: 2.1.257
variables:
  - TOOL_PARAMETER_ARTIFACT_VERSION_LABEL_VAR_0
  - TOOL_PARAMETER_ARTIFACT_VERSION_LABEL_VAR_1
-->
A short name for the version this publish${TOOL_PARAMETER_ARTIFACT_VERSION_LABEL_VAR_0?.TOOL_PARAMETER_ARTIFACT_VERSION_LABEL_VAR_1()?" (or `version`)":""} makes, max 60 chars (e.g. "Draft to legal"). Shown in the version picker. Optional — a few words, not a description.
