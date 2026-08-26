<!--
name: 'Tool Result: Artifact Create-From-Type Files Failed Own Files'
description: >-
  create-from-type files_leg_failed remedy when the error is type_owned_path:
  republish the Artifact's own files and leave type files out of
  file_path/files.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_FILES_FAILED_OWN_FILES_VAR_0
  - TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_FILES_FAILED_OWN_FILES_VAR_1
-->
publish this Artifact's own files to it with \`url\`: ${TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_FILES_FAILED_OWN_FILES_VAR_0(TOOL_RESULT_ARTIFACT_CREATE_FROM_TYPE_FILES_FAILED_OWN_FILES_VAR_1)}, leaving the type's files (listed next) out of \`file_path\`/\`files\`
