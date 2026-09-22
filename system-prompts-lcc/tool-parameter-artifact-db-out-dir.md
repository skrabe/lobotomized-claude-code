<!--
name: 'Tool Parameter: Artifact DB out_dir'
description: >-
  Artifact DB tool out_dir schema text telling the model to dump get/list/query
  documents as JSON files instead of inline contents.
ccVersion: 2.1.257
-->
get, list and query: when given, each returned document is written as pretty-printed JSON to <out_dir>/<collection path>/<doc_id>.json (directories created as needed) and the result lists the files instead of the document contents — use it for large documents or many of them.
