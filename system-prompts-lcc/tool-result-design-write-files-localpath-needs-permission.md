<!--
name: 'Tool result: design write_files localPath needs read permission'
description: >-
  write_files error when a localPath may not be read without asking the user
  (rule, network path, unresolvable link, or special Windows name); nothing was
  uploaded, stop and ask the user.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NEEDS_PERMISSION_VAR_0
  - TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NEEDS_PERMISSION_VAR_1
-->
write_files: the localPath for ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NEEDS_PERMISSION_VAR_0} may not be read without asking the user, and write_files can't ask. The cause is a ${TOOL_RESULT_DESIGN_WRITE_FILES_LOCALPATH_NEEDS_PERMISSION_VAR_1} rule or setting, a network path, a link that can't be resolved, or a name Windows treats specially (such as NAME~1, or one ending in a dot) in the file's name or in any folder above it. Nothing in this call was uploaded. Stop and ask the user how to proceed.
