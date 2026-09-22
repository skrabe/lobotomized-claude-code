<!--
name: 'Tool Description: Artifact Read Path Fetches'
description: >-
  Calls-section sentence that read with path fetches a published file or asset
  and reports where it was saved.
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_PATH_FETCHES_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_PATH_FETCHES_VAR_1
-->
 With \`path\`, it fetches ${TOOL_DESCRIPTION_ARTIFACT_READ_PATH_FETCHES_VAR_0.join(" or ")} instead and says where it put it${TOOL_DESCRIPTION_ARTIFACT_READ_PATH_FETCHES_VAR_1.multiFileOn?" (a small text file comes back inline, as data); with `paths` it fetches several published files in one call":""}.
