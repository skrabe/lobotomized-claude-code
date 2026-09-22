<!--
name: 'Tool Parameter: Artifact db data'
description: >-
  Artifact tool input-schema description of the `data` parameter carrying
  document fields for db_op set/update.
ccVersion: 2.1.273
-->
db_op 'set' (replaces the document) and 'update' (merges into it; a field given as `{"__delete__": true}` is removed) take exactly one of `data` or `file_path`; not accepted with any other db_op.
