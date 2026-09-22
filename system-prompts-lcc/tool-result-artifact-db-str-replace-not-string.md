<!--
name: 'Tool Result: Artifact DB Str Replace Not String'
description: write_db str_replace tool_result when the named field is not a string.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_0}: ${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_1} is not a string (str_replace edits top-level string fields only); nothing was written — use update for structured fields.${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NOT_STRING_VAR_2}
