<!--
name: Artifact delete — no artifact at that url
description: >-
  Deny message when the delete target probe returns boot_404: no artifact at
  that url, so nothing was deleted.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_NOT_FOUND_VAR_0
-->
There is no Artifact at ${TOOL_RESULT_ARTIFACT_DELETE_NOT_FOUND_VAR_0} — it may already be deleted, the link is wrong, or it isn't one the user can see. Nothing to delete; tell the user.
