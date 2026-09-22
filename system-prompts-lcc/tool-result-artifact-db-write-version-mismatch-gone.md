<!--
name: 'Tool Result: Artifact Db Write Version Mismatch Gone'
description: >-
  write_db error when an if_version pin no longer matches and the server named
  no current version, so the document may have been deleted.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_3
-->
${TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_0}: the document is no longer at version ${TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_1?.TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_2??"?"}, the one this write was pinned to — it has changed or may have been deleted; nothing was written. Read it back: if it still exists, re-plan the write against what it holds now and pin to its version; if it is gone, ${TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_1?.TOOL_RESULT_ARTIFACT_DB_WRITE_VERSION_MISMATCH_GONE_VAR_3==="delete"?"a delete has nothing left to do":'re-create it with a "set" and no if_version only if it should exist again'}
