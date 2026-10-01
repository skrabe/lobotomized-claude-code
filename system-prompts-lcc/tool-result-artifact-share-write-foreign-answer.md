<!--
name: 'Artifact Share: Write Foreign Answer'
description: >-
  Artifact share tool error when the relay's answer to the share write was not
  the artifact service's own; Claude must read the artifact before saying it is
  shared.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_WRITE_FOREIGN_ANSWER_VAR_0
-->
Couldn't confirm the share: the answer (HTTP ${TOOL_RESULT_ARTIFACT_SHARE_WRITE_FOREIGN_ANSWER_VAR_0.status}) was not the artifact service's own; read the artifact before telling the person it is shared.
