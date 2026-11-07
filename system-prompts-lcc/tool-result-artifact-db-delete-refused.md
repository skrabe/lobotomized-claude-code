<!--
name: 'Tool Result: Artifact database delete refused'
description: Explains why an artifact database delete was refused and not to retry it
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_ARTIFACT_DB_DELETE_REFUSED_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_DELETE_REFUSED_VAR_0}: the artifact's database refused this delete: the database has never been written to (so there is nothing to delete), the database's access rules or your access level do not let you delete there, or, less often, this artifact's data cannot be written right now; do not retry it
