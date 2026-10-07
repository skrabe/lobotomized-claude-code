<!--
name: 'Tool Description: Artifact read version'
description: Dynamic description for reading an earlier artifact version into a local file
ccVersion: 2.1.292
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_1
-->
Save ${typeof TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_0==="string"&&TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_1.test(TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_0)?`earlier version ${TOOL_DESCRIPTION_ARTIFACT_READ_VERSION_VAR_0}`:"an earlier version"} of a published artifact's page to a local file, as it was published (the artifact is not changed)
