<!--
name: 'Tool Result: Artifact DB Batch Write Stale Pin Changed Or Deleted'
description: >-
  version_mismatch tool result when a pinned document changed or may have been
  deleted with no current version.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_0}. ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_1} was pinned to version ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_2.ifVersion} and that document has changed or may have been deleted (the server named no current version): read it back — if it still exists, re-plan its write against what it holds now and pin to its version; if it is gone, drop that entry, or re-create it with a "set" entry and no if_version only if it should exist again. ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_STALE_PIN_CHANGED_OR_DELETED_VAR_3}
