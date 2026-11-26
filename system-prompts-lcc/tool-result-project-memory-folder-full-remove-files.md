<!--
name: 'Tool Result: Project in-memory folder full'
description: >-
  Clause telling Claude the session's in-memory folder for saved project files
  is full, to remove files it no longer needs beside earlier local_file paths,
  then call the tool again.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PROJECT_MEMORY_FOLDER_FULL_REMOVE_FILES_VAR_0
-->
the session's folder in memory for such files is full. Remove files there that you no longer need (they lie beside the local_file of earlier calls), then call ${TOOL_RESULT_PROJECT_MEMORY_FOLDER_FULL_REMOVE_FILES_VAR_0} again
