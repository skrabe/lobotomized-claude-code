<!--
name: 'Tool Result: Artifact Db Batch Write Missing If-Version'
description: >-
  Atomic batch write_db error when an unpinned entry targets an existing
  document, so the whole batch wrote nothing and those entries must be re-read
  and pinned.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_0}: writes[${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1.index}] (write ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1.index+1} of ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1.total}) targets ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1.path}, which already exists, and carried no if_version — the whole batch wrote nothing. Read that document back, re-plan its ${TOOL_RESULT_ARTIFACT_DB_BATCH_WRITE_MISSING_IF_VERSION_VAR_1.op==="delete"?"delete (if it should still be deleted)":"write on what it holds now"} with if_version set to the version the read returns, then resend the batch. ${"Other unpinned entries that write existing documents would be refused the same way — read and pin those too before resending"}
