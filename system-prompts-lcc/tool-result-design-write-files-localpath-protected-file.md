<!--
name: 'Tool result: design write_files localPath is a protected file'
description: >-
  write_files error when a localPath is or leads to a credential file, device or
  Claude Code's own config/token files; nothing was uploaded, stop and ask the
  user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_PROTECTED_FILE_VAR_0
-->
write_files: the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_PROTECTED_FILE_VAR_0} is or leads to a credential file, a device, or a file that Claude Code keeps for itself (its config and token folders), so it was not read. Nothing in this call was uploaded. Stop and ask the user how to proceed.
