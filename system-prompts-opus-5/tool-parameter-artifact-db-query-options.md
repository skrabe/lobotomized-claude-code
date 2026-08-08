<!--
name: 'Tool Parameter: Artifact db query options'
description: >-
  The `query` parameter description on the Artifact tool input schema, covering
  paging, where clauses and ordering for read_db list/query.
ccVersion: 2.1.224
-->
Options for db_op 'list' and 'query': `limit` and `cursor` (from a prior result's `next_cursor`) page through a collection; `where` clauses ([field, operator, value] triples) and `order_by` filter and order a 'query' only.
