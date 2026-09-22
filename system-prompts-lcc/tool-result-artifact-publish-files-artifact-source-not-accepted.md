<!--
name: 'Tool Result: Artifact Publish Files Artifact Source Not Accepted'
description: >-
  Input-validation error returned when a files entry uses the {artifact, path}
  copy source where it is not accepted. It tells Claude to publish the file from
  a local copy instead.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_ARTIFACT_SOURCE_NOT_ACCEPTED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_FILES_ARTIFACT_SOURCE_NOT_ACCEPTED_VAR_1
-->
files[${TOOL_RESULT_ARTIFACT_PUBLISH_FILES_ARTIFACT_SOURCE_NOT_ACCEPTED_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_FILES_ARTIFACT_SOURCE_NOT_ACCEPTED_VAR_1)}]: {artifact, path} is not accepted here. Publish this file from a local copy: a source path inside root, or {from, contentType}.
