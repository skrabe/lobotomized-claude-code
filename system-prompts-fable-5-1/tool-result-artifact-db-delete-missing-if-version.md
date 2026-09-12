<!--
name: 'Tool Result: Artifact Db Delete Missing If-Version'
description: >-
  write_db error when a delete targets an existing document with no if_version
  pin, so nothing was deleted and the model must re-read and resend with a pin.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_ARTIFACT_DB_DELETE_MISSING_IF_VERSION_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_DELETE_MISSING_IF_VERSION_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DB_DELETE_MISSING_IF_VERSION_VAR_0}: ${TOOL_RESULT_ARTIFACT_DB_DELETE_MISSING_IF_VERSION_VAR_1} is an existing document and this delete carried no if_version — nothing was deleted. Read it back and, if it should still be deleted, resend the delete with if_version set to the version that read returns
