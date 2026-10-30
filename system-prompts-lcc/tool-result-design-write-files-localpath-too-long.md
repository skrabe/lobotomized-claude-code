<!--
name: 'Tool result: design write_files localPath too long'
description: >-
  write_files error when the full localPath is longer than the character limit;
  nothing was uploaded, stop and ask the user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_TOO_LONG_VAR_0
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_TOO_LONG_VAR_1
-->
write_files: the full path of the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_TOO_LONG_VAR_0} is longer than ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_TOO_LONG_VAR_1} characters, so it was not read. Nothing in this call was uploaded. Stop and ask the user how to proceed.
