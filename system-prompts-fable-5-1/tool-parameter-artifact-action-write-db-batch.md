<!--
name: 'Tool Parameter: Artifact Action write_db Batch'
description: >-
  Continuation of the action-enum description after the batch size concat,
  covering all-or-nothing batch writes and the untrusted shared-db caveat.
ccVersion: 2.1.251
-->
 of those as {op, collection, doc_id, data or file_path} entries) applies them under one approval — all-or-nothing where the server supports batches, otherwise one at a time in order (the result says which) — prefer it whenever writing more than a couple of documents.
