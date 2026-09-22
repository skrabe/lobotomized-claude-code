<!--
name: 'Tool Parameter: Artifact database version precondition'
description: >-
  Defines the optional if_version precondition for Artifact database writes,
  directing Claude to supply the last-read document version and pin batch
  entries individually
ccVersion: 2.1.267
-->
write_db with db_op 'set', 'update', 'str_replace' or 'delete' (a 'batch' pins each entry in `writes` instead): the document's `version` as you last read it (every read_db document carries it, and so does every set, update and str_replace result). Pass it on every write to a document you have read: the write applies only if the document is still at that version; otherwise nothing is written and the result names the current version — so pin the write instead of re-reading first to check. Optional; omit it only for a document you have not read.
