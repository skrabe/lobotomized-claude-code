<!--
name: 'Tool Result: Artifact DB Str Replace Ambiguous'
description: >-
  write_db str_replace tool_result when old_str occurs more than once in a
  document field.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_0}: old_str occurs more than once in ${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_1} of that document; nothing was written.${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_AMBIGUOUS_VAR_2} Include more surrounding text so it is unique, or pass replace_all to change every occurrence
