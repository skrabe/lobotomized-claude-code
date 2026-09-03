<!--
name: 'Tool Description: Artifact Watching Unavailable With Status'
description: >-
  Artifact prompt section when watching is unavailable, still documenting
  status/unwatch verbs.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_2
-->
**Watching for republishes**: not available in this session — nothing notifies it when an artifact is republished elsewhere${TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_0?" or when a comment on one is sent to Claude":""}, and \`action: "watch"\` only reports that${TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_1()}. If the user asks you to watch an artifact, say so plainly. \`action: "status"\` lists this session's watches (pass \`url\` to check one); \`action: "unwatch"\` with \`url\` stops one. Do not claim you are watching an artifact.${TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_0?"":TOOL_DESCRIPTION_ARTIFACT_WATCHING_UNAVAILABLE_WITH_STATUS_VAR_2}
