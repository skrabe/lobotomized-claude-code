<!--
name: 'Data: Artifact Opening More Saved Files'
description: >-
  Truncation bullet in the opening-context saved-file list when more files were
  written than the listing budget.
ccVersion: 2.1.273
variables:
  - DATA_ARTIFACT_OPENING_MORE_SAVED_FILES_VAR_0
  - DATA_ARTIFACT_OPENING_MORE_SAVED_FILES_VAR_1
-->
- and ${DATA_ARTIFACT_OPENING_MORE_SAVED_FILES_VAR_0.files.length-DATA_ARTIFACT_OPENING_MORE_SAVED_FILES_VAR_1} more saved files in that folder, under the names the system gives them
