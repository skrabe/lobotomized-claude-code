<!--
name: 'Tool Parameter: Artifact write_db if_version'
description: >-
  Zod .describe() on write_db db_op 'update' or 'str_replace' `if_version`: pin
  the write to the document version last read.
ccVersion: 2.1.265
-->
write_db with db_op 'update' or 'str_replace' only: the document's `version` as you last read it (every read_db document and every write result carries it). The write applies only if the document is still at that version; otherwise nothing is written and the result names the current version — so pin the edit instead of re-reading first to check.
