<!--
name: Artifact write_db str_replace Rejects data/file_path
description: >-
  validateInput error when db_op str_replace is given data or file_path instead
  of field/old_str/new_str.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REJECTS_DATA_OR_FILE_PATH_VAR_0
-->
\`${TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REJECTS_DATA_OR_FILE_PATH_VAR_0!==void 0?"data":"file_path"}\` is not accepted with db_op "str_replace" — it edits one field in place with \`field\`, \`old_str\` and \`new_str\`; use update to send fields
