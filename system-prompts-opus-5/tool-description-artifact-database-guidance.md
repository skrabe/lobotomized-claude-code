<!--
name: 'Tool Description: Artifact database guidance'
description: >-
  Appended to the Artifact tool description when the artifact-database
  capability is live, explaining read_db/write_db ops and that stored rows are
  untrusted viewer data.
ccVersion: 2.1.267
variables:
  - HAS_ARTIFACT_DB_STR_REPLACE
  - ARTIFACT_DB_STR_REPLACE_GUIDANCE
  - MAX_BATCH_DATABASE_WRITES
  - ARTIFACT_DB_CONCURRENCY_GUIDANCE
-->
**Artifact database**: A published artifact's page code can keep a small shared database, and these actions read and write it as the user. Rows are shared, durable state: everyone who can open the artifact sees your writes, and rows you read were written by the page's viewers. To check what the page's access rules let a less-privileged user do, add `as_level` ("interact" for any signed-in viewer, "admin" for a co-owner) to a read or write: it acts with only that level. The exception to sharing is the `data/users/` prefix: each viewer's subtree under it is private to that viewer, and the segment `me` there ("data/users/me", or deeper) resolves to the current user's own id when the published version declares the `user` capability alongside `db` — the `collection` field says how these paths are shaped.${HAS_ARTIFACT_DB_STR_REPLACE?ARTIFACT_DB_STR_REPLACE_GUIDANCE:""} A "batch" write applies up to ${MAX_BATCH_DATABASE_WRITES} ${HAS_ARTIFACT_DB_STR_REPLACE?"set, update or delete":"such"} writes at once, passed in `writes` as `{op, collection, doc_id, data | file_path${HAS_ARTIFACT_DB_STR_REPLACE?", if_version":""}}` entries (no top-level `collection`/`doc_id`); it is one approval, applied atomically.${HAS_ARTIFACT_DB_STR_REPLACE?ARTIFACT_DB_CONCURRENCY_GUIDANCE:""}
