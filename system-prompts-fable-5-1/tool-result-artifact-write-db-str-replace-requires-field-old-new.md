<!--
name: Artifact write_db str_replace Requires field/old_str/new_str
description: >-
  validateInput error listing the missing field, old_str, and/or new_str
  required for db_op str_replace.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REQUIRES_FIELD_OLD_NEW_VAR_0
  - TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REQUIRES_FIELD_OLD_NEW_VAR_1
-->
db_op "str_replace" requires ${TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REQUIRES_FIELD_OLD_NEW_VAR_0.map((TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REQUIRES_FIELD_OLD_NEW_VAR_1)=>`\`${TOOL_RESULT_ARTIFACT_WRITE_DB_STR_REPLACE_REQUIRES_FIELD_OLD_NEW_VAR_1}\``).join(", ")} — the top-level string field to edit, the exact text to replace (it must occur exactly once in that field), and its replacement (\`new_str\` may be "" to delete it).
