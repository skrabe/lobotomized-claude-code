<!--
name: 'Tool Parameter: Artifact out_dir — read_db'
description: >-
  out_dir schema description for read_db: write each document as JSON under
  out_dir and list the files instead of returning contents.
ccVersion: 2.1.237
-->
read_db: when given, each returned document is written as pretty-printed JSON to <out_dir>/<collection path>/<doc_id>.json (directories created as needed) and the result lists the files instead of the document contents — use it for large documents or many of them.
