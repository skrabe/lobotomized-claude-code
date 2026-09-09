<!--
name: 'Tool Result: Artifact write_db old_str No Match (Pinned)'
description: >-
  write_db str_replace tool_result when old_str is missing and the edit was
  pinned to the document's current version, so the stored text never matched.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_0
  - TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_1
  - TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_2
  - TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_0}: old_str does not occur in ${TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_1} of that document, so nothing was written by this call. The document is still at version ${TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_2?.TOOL_RESULT_ARTIFACT_WRITE_DB_OLD_STR_NO_MATCH_PINNED_VAR_3}, the one this edit was pinned to, so nothing changed under you: old_str itself does not match the stored text — copy it exactly as it appears in the field's value (the decoded string, not JSON-escaped source)
