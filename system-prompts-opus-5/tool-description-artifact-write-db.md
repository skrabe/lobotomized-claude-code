<!--
name: 'Tool Description: Artifact write_db'
description: >-
  Dynamic Artifact tool description for write_db, including session-scoped
  approval coverage and the per-write exception clause.
ccVersion: 2.1.237
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_3
  - TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_4
-->
${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_0(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_1)?"Write a local JSON file's content to a published artifact's database":"Write data to a published artifact's database"}${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_2(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_3)} — the write is durable (${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_4}); approving covers database writes to any artifact for the rest of this session${TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_0(TOOL_DESCRIPTION_ARTIFACT_WRITE_DB_VAR_1)?" — except in auto mode, or when the file needs its own Read approval (outside the working paths, matched by a Read ask rule, or reached through a link), where each such write asks again":""}.
