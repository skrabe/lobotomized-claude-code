<!--
name: Artifact delete refused — not the owner
description: >-
  Deny message when the Artifact at the given url belongs to someone else and
  only its owner can delete it.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_NOT_OWNER_VAR_0
-->
The Artifact at ${TOOL_RESULT_ARTIFACT_DELETE_NOT_OWNER_VAR_0} belongs to someone else, and only its owner can delete it. Nothing was deleted; tell the user.
