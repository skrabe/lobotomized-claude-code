<!--
name: 'Tool Result: Artifact Share Ownership Unconfirmed'
description: >-
  checkPermissions deny when the person's ownership of the Artifact could not be
  confirmed before a share; nothing was shared
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_OWNERSHIP_UNCONFIRMED_VAR_0
  - TOOL_RESULT_ARTIFACT_SHARE_OWNERSHIP_UNCONFIRMED_VAR_1
-->
Couldn't confirm that the person owns the Artifact at ${TOOL_RESULT_ARTIFACT_SHARE_OWNERSHIP_UNCONFIRMED_VAR_0}, so nothing was shared. Retry once; if it still fails, ${TOOL_RESULT_ARTIFACT_SHARE_OWNERSHIP_UNCONFIRMED_VAR_1}
