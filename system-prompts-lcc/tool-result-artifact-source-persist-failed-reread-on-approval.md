<!--
name: 'Tool Result: Artifact source persist failed, re-read needs approval'
description: >-
  Artifact tool result when the source could not be shown inline or saved to
  disk, telling the model to re-read it (which asks the user to approve), and
  not to republish from a summary, truncated or inexact copy
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_SOURCE_PERSIST_FAILED_REREAD_ON_APPROVAL_VAR_0
-->
Its source could not be shown inline and saving it to disk failed here. Re-read it (${TOOL_RESULT_ARTIFACT_SOURCE_PERSIST_FAILED_REREAD_ON_APPROVAL_VAR_0}) — that read asks the user to approve reading this artifact and, once they approve, it arrives inline if it fits; if they decline, or it comes back TRUNCATED or marked as not the exact bytes, tell the user, and do not republish from a summary or such a copy.
