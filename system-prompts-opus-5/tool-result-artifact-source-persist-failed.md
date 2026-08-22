<!--
name: 'Tool Result: Artifact source could not be persisted'
description: >-
  Artifact publish-conflict clause telling the model the newer source could
  neither be shown inline nor written to disk, to re-read it, and never to
  republish from a TRUNCATED copy
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_SOURCE_PERSIST_FAILED_VAR_0
-->
Its source could not be shown inline and saving it to disk failed here. Re-read it (${TOOL_RESULT_ARTIFACT_SOURCE_PERSIST_FAILED_VAR_0}) — it arrives inline if it fits; if it comes back TRUNCATED, tell the user, and do not republish from a truncated copy.
