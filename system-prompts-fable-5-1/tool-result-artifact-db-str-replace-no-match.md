<!--
name: 'Tool Result: Artifact DB Str-Replace No Match'
description: >-
  Unpinned write_db str_replace tool-result when old_str is absent, telling the
  model to copy the decoded field value and re-read before retrying.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_2
-->
${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_0}: old_str does not occur in ${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_1} of that document, so nothing was written by this call.${TOOL_RESULT_ARTIFACT_DB_STR_REPLACE_NO_MATCH_VAR_2} Copy the text exactly as it appears in the field's value (the decoded string, not JSON-escaped source). If you were retrying after a call whose outcome you did not see, that earlier call may already have applied — read the document back before trying again. If someone else changed that text, re-read and re-plan the edit
