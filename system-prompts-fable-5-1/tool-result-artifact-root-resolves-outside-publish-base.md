<!--
name: 'Tool Result: Artifact Root Resolves Outside Publish Base'
description: >-
  Validation error returned to the model when publish root's realpath lies
  outside the allowed publish base.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_0
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_1
  - TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_2
-->
root: ${TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_0.stringify(TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_1)} resolves outside ${TOOL_RESULT_ARTIFACT_ROOT_RESOLVES_OUTSIDE_PUBLISH_BASE_VAR_2} — the publish base must lie within it
