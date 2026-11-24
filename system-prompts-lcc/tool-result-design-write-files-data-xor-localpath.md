<!--
name: write_files data XOR localPath
description: >-
  DesignSync validateInput error returned to the model when a write_files file
  lacks localPath or also carries data.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_DATA_XOR_LOCALPATH_VAR_0
-->
Each file needs "localPath", and "data" can't go with it (offending path: ${TOOL_RESULT_DESIGN_WRITE_FILES_DATA_XOR_LOCALPATH_VAR_0.path}).
