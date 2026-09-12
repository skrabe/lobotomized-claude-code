<!--
name: 'Tool Result: Artifact DB Update Missing If-Version'
description: >-
  write_db tool_result when an update targeted an existing document with no
  if_version, so nothing was written.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_ARTIFACT_DB_UPDATE_MISSING_IF_VERSION_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_UPDATE_MISSING_IF_VERSION_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DB_UPDATE_MISSING_IF_VERSION_VAR_0}: ${TOOL_RESULT_ARTIFACT_DB_UPDATE_MISSING_IF_VERSION_VAR_1} is an existing document and this update carried no if_version — nothing was written. ${"Read it back with read_db, base the change on what it holds now, and resend with if_version set to the version that read returns"}
