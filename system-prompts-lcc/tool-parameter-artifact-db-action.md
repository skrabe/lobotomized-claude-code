<!--
name: 'Tool Parameter: Artifact DB Action'
description: >-
  Artifact DB tool action enum describing get/list/query reads and
  set/update/delete/batch writes.
ccVersion: 2.1.265
variables:
  - TOOL_PARAMETER_ARTIFACT_DB_ACTION_VAR_0
-->
Reads: 'get' (one document: `collection` + `doc_id`), 'list' (a page of a collection: `collection`, with optional `query.limit`/`query.cursor`), 'query' (filtered: `collection` + `query`). Writes: 'set' (replace) or 'update' (merge) with `collection`, `doc_id`, and either `data` or `file_path`;${TOOL_PARAMETER_ARTIFACT_DB_ACTION_VAR_0?" 'str_replace' with `collection`, `doc_id`, `field`, `old_str`, `new_str` — swaps one exact, unique piece of text inside a string field without resending the field (`replace_all`: every occurrence);":""} 'delete' with `collection` + `doc_id`; 'batch' with `writes`. Every action takes the artifact's `url`.
