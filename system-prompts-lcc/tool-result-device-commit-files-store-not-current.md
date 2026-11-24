<!--
name: 'Tool result: device_commit_files store not current'
description: >-
  Error from device_commit_files when the newest version of a file may not be
  stored yet, with retry and fallback steps.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_DEVICE_COMMIT_FILES_STORE_NOT_CURRENT_VAR_0
  - TOOL_RESULT_DEVICE_COMMIT_FILES_STORE_NOT_CURRENT_VAR_1
-->
Nothing was copied: the newest version of a file in this call may not be stored yet. Make sure nothing is still writing these files or holding them open, wait ten seconds, and call device_commit_files again. If it fails again, copy the files one call at a time to find the one that waits. For that file, call ${TOOL_RESULT_DEVICE_COMMIT_FILES_STORE_NOT_CURRENT_VAR_0} now, if you have it, and pass the new fileUuid in place of stagedPath, or tell the user that it could not be saved yet. A file under ${TOOL_RESULT_DEVICE_COMMIT_FILES_STORE_NOT_CURRENT_VAR_1} also waits while the project's storage is full.
