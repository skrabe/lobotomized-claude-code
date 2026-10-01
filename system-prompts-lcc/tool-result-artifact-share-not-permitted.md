<!--
name: 'Tool result: Artifact share not permitted'
description: >-
  Artifact share error on HTTP 403: the person isn't allowed to change this
  artifact's sharing from here (with optional detail), and only its owner can.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_NOT_PERMITTED_VAR_0
-->
The person isn't allowed to change this artifact's sharing from here${TOOL_RESULT_ARTIFACT_SHARE_NOT_PERMITTED_VAR_0?` (${TOOL_RESULT_ARTIFACT_SHARE_NOT_PERMITTED_VAR_0})`:""}; nothing was changed. Only its owner can, within what their organization allows — and a cloud session without network access only for artifacts it created. The person can use the Share menu on claude.ai.
