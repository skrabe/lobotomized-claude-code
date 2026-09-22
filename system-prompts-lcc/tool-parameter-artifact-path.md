<!--
name: 'Tool Parameter: Artifact Path'
description: >-
  Artifact-tool path parameter naming the file's published path inside the
  artifact exactly as list_files printed it, with index.html being the page.
ccVersion: 2.1.257
variables:
  - TOOL_PARAMETER_ARTIFACT_PATH_VAR_0
-->
read_file${TOOL_PARAMETER_ARTIFACT_PATH_VAR_0?"":" only"}: the file's published path inside the artifact, exactly as list_files printed it; "index.html" is the page itself.
