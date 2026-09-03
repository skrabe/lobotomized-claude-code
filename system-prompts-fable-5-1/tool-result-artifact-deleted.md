<!--
name: 'Tool Result: Artifact deleted'
description: >-
  Artifact delete tool result confirming the artifact (or an already-gone one)
  is permanently removed, its comments and history are lost, and the url must
  not be reused
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DELETED_VAR_0
  - TOOL_RESULT_ARTIFACT_DELETED_VAR_1
-->
${TOOL_RESULT_ARTIFACT_DELETED_VAR_0.already_gone===!0?`The Artifact at ${TOOL_RESULT_ARTIFACT_DELETED_VAR_1} was already deleted`:`Artifact deleted: ${TOOL_RESULT_ARTIFACT_DELETED_VAR_1}`}. Its link no longer works for anyone, its comments and version history are gone, and it cannot be restored. Do not pass this url again — publishing the same file again creates a new Artifact at a new URL. If the user still wants the content, give it to them the way they asked (for example, the local file).
