<!--
name: 'Tool result: design write_files localPath is a hard link'
description: >-
  write_files error when the file at a localPath is a hard link whose other name
  cannot be permission-checked; nothing was uploaded, stop and ask the user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_HARD_LINK_VAR_0
-->
write_files: the file at the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_HARD_LINK_VAR_0} is a hard link (it has another name elsewhere whose read permission can't be checked), so it was not read. Nothing in this call was uploaded. Stop and ask the user how to proceed.
