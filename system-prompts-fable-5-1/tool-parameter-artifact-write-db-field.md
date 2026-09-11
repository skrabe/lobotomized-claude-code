<!--
name: 'Tool Parameter: Artifact write_db field'
description: >-
  Schema description of write_db str_replace field: the top-level string key of
  the document to edit, with length and character constraints.
ccVersion: 2.1.268
-->
write_db with db_op 'str_replace' only: the top-level string field of the document to edit — one plain key, e.g. "html" (1-200 bytes; no dots, slashes, brackets, quotes, backslashes, control or invisible formatting characters; not a reserved __name__ key).
