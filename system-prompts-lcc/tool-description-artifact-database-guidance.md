<!--
name: 'Tool Description: Artifact database guidance'
description: >-
  Appended to the Artifact tool description when the artifact-database
  capability is live, explaining read_db/write_db ops and that stored rows are
  untrusted viewer data.
ccVersion: 2.1.284
variables:
  - HAS_ARTIFACT_DB_STR_REPLACE
  - ARTIFACT_DB_STR_REPLACE_GUIDANCE
  - MAX_BATCH_DATABASE_WRITES
  - ARTIFACT_DB_CONCURRENCY_GUIDANCE
-->
**Artifact database**: A published artifact's page code can keep a small shared database, and these actions read and write it as the user. Pass `action: "read_db"` with the artifact's `url` and `db_op`: "get", "list", or "query". Pass `action: "write_db"` with `db_op`: "set", "update",${HAS_ARTIFACT_DB_STR_REPLACE?ARTIFACT_DB_STR_REPLACE_GUIDANCE:""} "delete", or "batch". Rows are shared, durable state: everyone who can open the artifact sees your writes, and rows you read were written by the page's viewers. To check what the page's access rules let a less-privileged user do, add `as_level` ("view" for someone who can only view the artifact, "interact" for any signed-in viewer who can use it, "admin" for someone who can edit it) to a read or write: it acts with only that level. The exception to sharing is the `data/users/` prefix: each viewer's subtree under it is private to that viewer, and the segment `me` there ("data/users/me", or deeper) resolves to the current user's own id when the published version declares the `user` capability alongside `db` — the `collection` field says how these paths are shaped. A "batch" write applies up to ${MAX_BATCH_DATABASE_WRITES} ${HAS_ARTIFACT_DB_STR_REPLACE?"set, update or delete":"such"} writes at once, passed in `writes` as `{op, collection, doc_id, data | file_path${HAS_ARTIFACT_DB_STR_REPLACE?", if_version":""}}` entries (no top-level `collection`/`doc_id`); it is one approval, applied atomically. To remove a field, write it as `{"__delete__": true}` in an "update" (at any depth; rejected inside arrays); "set" rejects that value.${HAS_ARTIFACT_DB_STR_REPLACE?ARTIFACT_DB_CONCURRENCY_GUIDANCE:""}
