<!--
name: 'Artifact Share: Read Foreign Answer'
description: >-
  Artifact share tool error when the relay's answer to the sharing read was not
  the artifact service's own; nothing changed, retry once.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_READ_FOREIGN_ANSWER_VAR_0
-->
Couldn't read the artifact's sharing settings: the answer (HTTP ${TOOL_RESULT_ARTIFACT_SHARE_READ_FOREIGN_ANSWER_VAR_0.status}) was not the artifact service's own; nothing was changed. Retry once.
