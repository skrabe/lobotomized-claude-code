<!--
name: Artifact Read Path Saves Local File
description: >-
  Artifact tool-description clause that path on read saves the chosen content to
  a local file and reports where.
ccVersion: 2.1.265
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_PATH_SAVES_LOCAL_FILE_VAR_0
-->
 With \`path\` it saves ${TOOL_DESCRIPTION_ARTIFACT_READ_PATH_SAVES_LOCAL_FILE_VAR_0.join(" or ")} to a local file instead and says where${TOOL_DESCRIPTION_ARTIFACT_READ_PATH_SAVES_LOCAL_FILE_VAR_1.multiFileOn?"; a small published text file's contents also come back in the result, as data, so you need not Read it":""}.
