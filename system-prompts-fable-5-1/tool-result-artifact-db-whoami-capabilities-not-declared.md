<!--
name: 'Tool Result: Artifact DB Whoami Capabilities Missing'
description: >-
  Tells the model that resolving the current user requires republishing with
  database and user capabilities declared.
ccVersion: 2.1.228
variables:
  - TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_2
-->
db ${TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_0} failed (${TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_1(TOOL_RESULT_ARTIFACT_DB_WHOAMI_CAPABILITIES_NOT_DECLARED_VAR_2)}): resolving 'me' needs this artifact's published version to declare the db and user capabilities — republish with both declared, then retry
