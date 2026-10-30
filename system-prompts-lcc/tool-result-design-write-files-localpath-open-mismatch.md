<!--
name: 'Tool result: design write_files localPath opened file mismatch'
description: >-
  write_files error when the file at a localPath could not be opened as the file
  that was checked; nothing uploaded, retry once then stop and ask the user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_OPEN_MISMATCH_VAR_0
-->
write_files: the file at the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_OPEN_MISMATCH_VAR_0} could not be opened as the file that was checked (it may have been moved or replaced, or the system would not say which file was opened), so it was not read. Nothing in this call was uploaded. Try the call once more; if it fails again, stop and ask the user how to proceed.
