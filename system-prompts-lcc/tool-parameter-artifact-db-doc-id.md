<!--
name: 'Tool Parameter: Artifact db doc_id'
description: >-
  Artifact tool input-schema description of the `doc_id` parameter identifying a
  single database document.
ccVersion: 2.1.265
variables:
  - TOOL_PARAMETER_ARTIFACT_DB_DOC_ID_VAR_0
-->
Document id (one path segment). Required for db_op 'get', 'set', 'update'${TOOL_PARAMETER_ARTIFACT_DB_DOC_ID_VAR_0?", 'str_replace'":""} and 'delete'; not accepted with 'list' or 'query'.
