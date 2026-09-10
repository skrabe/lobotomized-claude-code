<!--
name: 'Tool Parameter: Artifact write_db Batch Writes'
description: >-
  Artifact tool input-schema description of write_db db_op 'batch' writes:
  all-or-nothing set/update/delete entries.
ccVersion: 2.1.267
variables:
  - TOOL_PARAMETER_ARTIFACT_WRITE_DB_BATCH_WRITES_VAR_0
  - TOOL_PARAMETER_ARTIFACT_WRITE_DB_BATCH_WRITES_VAR_1
-->
write_db with db_op 'batch' only: the writes to apply together, 1-${TOOL_PARAMETER_ARTIFACT_WRITE_DB_BATCH_WRITES_VAR_0} entries of {op: 'set'|'update'|'delete', collection, doc_id, and for set/update exactly one of data (inline object) or file_path (a local JSON file)${TOOL_PARAMETER_ARTIFACT_WRITE_DB_BATCH_WRITES_VAR_1?", plus if_version — that document's last-read `version` (optional; omit it only for a document you have not read); if any pinned document has changed since, the whole batch writes nothing and the result names the entry and its current version":""}}. Each document is addressed at most once; the batch commits all-or-nothing where the server supports it, else ${TOOL_PARAMETER_ARTIFACT_WRITE_DB_BATCH_WRITES_VAR_1?"(a batch with no pinned entry) ":""}in order one at a time (the result says which).
