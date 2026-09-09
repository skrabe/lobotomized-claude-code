<!--
name: 'Tool Description: Artifact database guidance'
description: >-
  Appended to the Artifact tool description when the artifact-database
  capability is live, explaining read_db/write_db ops and that stored rows are
  untrusted viewer data.
ccVersion: 2.1.265
variables:
  - MAX_BATCH_DATABASE_WRITES
  - TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_3
-->
**Artifact database**: A published artifact's page code can keep a small shared database, and these actions read and write it as the user. Rows are shared, durable state: everyone who can open the artifact sees your writes, and rows you read were written by the page's viewers. To check what the page's access rules let a less-privileged user do, add `as_level` ("interact" for any signed-in viewer, "admin" for a co-owner) to a read or write: it acts with only that level. The exception to sharing is the `data/users/` prefix: each viewer's subtree under it is private to that viewer, and the segment `me` there ("data/users/me", or deeper) resolves to the current user's own id when the published version declares the `user` capability alongside `db` — the `collection` field says how these paths are shaped.${MAX_BATCH_DATABASE_WRITES?TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_1:""} A "batch" write applies up to ${TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_2} ${MAX_BATCH_DATABASE_WRITES?"set, update or delete":"such"} writes at once, passed in `writes` as `{op, collection, doc_id, data | file_path}` entries (no top-level `collection`/`doc_id`); it is one approval, applied atomically.${MAX_BATCH_DATABASE_WRITES?TOOL_DESCRIPTION_ARTIFACT_DATABASE_GUIDANCE_VAR_3:""}
