<!--
name: write_files data XOR localPath
description: >-
  DesignSync validateInput error returned to the model when a file lacks exactly
  one of data/localPath.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_DATA_XOR_LOCALPATH_VAR_0
-->
Each file needs exactly one of "data" or "localPath" (offending path: ${TOOL_RESULT_DESIGN_WRITE_FILES_DATA_XOR_LOCALPATH_VAR_0.path}).
