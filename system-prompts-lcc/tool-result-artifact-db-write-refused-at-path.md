<!--
name: 'Tool Result: Artifact database write refused at path'
description: >-
  Explains an artifact database write refused at its path, usually access rules,
  not applied, do not retry
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_REFUSED_AT_PATH_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_WRITE_REFUSED_AT_PATH_VAR_0}: the artifact's database refused this write at its path, most often because the database's access rules or your access level do not allow it (less often, this artifact's data cannot be written right now); this write was not applied — do not retry it
