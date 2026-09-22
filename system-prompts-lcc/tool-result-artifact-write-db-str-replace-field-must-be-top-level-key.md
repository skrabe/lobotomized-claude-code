<!--
name: Artifact write_db str_replace Field Must Be Top-Level Key
description: >-
  validateInput error when field is not a single top-level document key (nested
  paths belong on update).
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_FIELD_MUST_BE_TOP_LEVEL_KEY_VAR_0
-->
\`field\` must name one top-level key of the document (1-${TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_FIELD_MUST_BE_TOP_LEVEL_KEY_VAR_0} bytes; no dots, slashes, brackets, quotes, control or invisible formatting characters; not a reserved __name__ key) — str_replace edits a top-level string field, not a path into nested data; use update for nested fields.
