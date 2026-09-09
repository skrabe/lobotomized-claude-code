<!--
name: 'Tool Result: Artifact File Listing Record Unreadable'
description: >-
  list_files tool_result when the stored file_list record fails to parse,
  telling the model to list again.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_FILE_LIST_RECORD_UNREADABLE_VAR_0
-->
This record of a file listing is unreadable — run ${TOOL_RESULT_ARTIFACT_FILE_LIST_RECORD_UNREADABLE_VAR_0('action "list_files"',()=>'action "list" with `scope: "files"`')} again for the live listing.
