<!--
name: 'Tool Parameter: Artifact out_dir for read_file'
description: >-
  read_file branch of the Artifact out_dir parameter, naming the scratchpad
  default that needs no approval and where the file lands under a custom
  directory
ccVersion: 2.1.273
variables:
  - TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_0
  - TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_1
  - TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_2
-->
${[TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_0&&"read_asset",TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_1&&"read_file"].filter(TOOL_PARAMETER_ARTIFACT_OUT_DIR_READ_FILE_VAR_2).join(" / ")}: directory to save into — default: this artifact’s folder in your scratchpad directory, where saving needs no approval and which you can Read from.
