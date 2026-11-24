<!--
name: 'Tool Result: DesignSync localPath not the file'
description: >-
  write_files error when localPath is not the file at that path in the approved
  folder.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NOT_THE_FILE_VAR_0
-->
write_files: the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NOT_THE_FILE_VAR_0} must be the file at that path in the folder approved at finalize_plan, not another file or a link to one. It was not read, and nothing in this call was uploaded. Pass that file, call finalize_plan again with the right folder and paths, or stop and ask the user how to proceed.
