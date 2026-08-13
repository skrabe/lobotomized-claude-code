<!--
name: 'Tool Parameter: Artifact Action read_db / write_db'
description: >-
  Segment of the Artifact tool's `action` enum description covering read_db and
  write_db, their db_op values, cursor paging, and the
  shared-state/untrusted-rows caveat.
ccVersion: 2.1.231
-->
 'read_db' reads the artifact's shared database: pass `url` and `db_op` — 'get' (one document: `collection` + `doc_id`), 'list' (a page of a collection: `collection`, with optional `query.limit`/`query.cursor`), or 'query' (filtered: `collection` + `query`). A result carrying `next_cursor` has more pages — pass it back as `query.cursor` instead of re-fetching documents one by one. 'write_db' changes the database: `db_op` 'set' (replace) or 'update' (merge) with `collection`, `doc_id`, `data`; 'delete' with `collection` + `doc_id`. The 'data/users/' prefix is the exception — each viewer's subtree under it is private to that viewer — and the literal segment 'me' directly after 'data/users' (collection 'data/users/me' or deeper, or `doc_id` 'me' under collection 'data/users') resolves to the current user's own id, the one the page reads from `claude.user.id()`; it requires the artifact's published version to declare the user capability alongside db.
