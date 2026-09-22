<!--
name: 'Tool Result: Artifact Publish Target Gone Type-Create Remedy'
description: >-
  publish_target_gone remedy telling the model to pass `type_url` or the
  type-created Artifact's `url` to publish the file again.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_TYPE_CREATE_REMEDY_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_TYPE_CREATE_REMEDY_VAR_1
-->
To publish this file again it needs another Artifact created from an Artifact type: ${TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_TYPE_CREATE_REMEDY_VAR_0().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_TYPE_CREATE_REMEDY_VAR_1===!0?"pass `type_url` to create one from its type":"pass that Artifact's `url`"}
