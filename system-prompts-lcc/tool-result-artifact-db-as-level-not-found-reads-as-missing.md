<!--
name: Artifact DB as_level Not-Found Reads As Missing
description: >-
  Cu() suffix on a db_write error when as_level was requested and the server
  reported not_found, so a page-rule refusal is indistinguishable from absence.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_NOT_FOUND_READS_AS_MISSING_VAR_0
-->
 (as_level '${TOOL_RESULT_ARTIFACT_DB_AS_LEVEL_NOT_FOUND_READS_AS_MISSING_VAR_0}' was requested: if the server applied it, a refusal by the page's access rules reads as not found)
