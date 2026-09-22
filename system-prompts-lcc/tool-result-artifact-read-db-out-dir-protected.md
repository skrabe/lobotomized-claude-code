<!--
name: 'Tool Result: Artifact read_db out_dir Protected'
description: >-
  checkPermissions deny when read_db would save documents to a path the
  file-edit safety rules protect.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_READ_DB_OUT_DIR_PROTECTED_VAR_0
-->
read_db does not save artifact database documents as ${TOOL_RESULT_ARTIFACT_READ_DB_OUT_DIR_PROTECTED_VAR_0}: the file-edit safety rules protect that location or name. Choose another out_dir, or read the documents without out_dir.
