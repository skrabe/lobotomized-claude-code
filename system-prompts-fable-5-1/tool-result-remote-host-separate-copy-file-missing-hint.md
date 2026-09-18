<!--
name: 'Tool Result: Remote Host Separate Copy File-Missing Hint'
description: >-
  Suffix appended to Read/Glob/Grep not-found errors when an attached machine
  holds the user's own unsynced copy of the project, pointing the model at the
  served tool on that machine.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_REMOTE_HOST_SEPARATE_COPY_FILE_MISSING_HINT_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SEPARATE_COPY_FILE_MISSING_HINT_VAR_1
-->
 ${TOOL_RESULT_REMOTE_HOST_SEPARATE_COPY_FILE_MISSING_HINT_VAR_0.name} holds the user's own separate copy of this project (nothing is synced between it and this session's checkout, and it may be at a different commit); if the file exists only in that copy, use ${TOOL_RESULT_REMOTE_HOST_SEPARATE_COPY_FILE_MISSING_HINT_VAR_1}.
