<!--
name: 'Artifact share: unexpected fields'
description: Artifact share validation error listing fields the share action does not take.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_UNEXPECTED_FIELDS_VAR_0
-->
action "share" takes only \`url\`, \`mode\`, \`people\` and \`access\` — remove ${TOOL_RESULT_ARTIFACT_SHARE_UNEXPECTED_FIELDS_VAR_0.join(", ")}.${TOOL_RESULT_ARTIFACT_SHARE_UNEXPECTED_FIELDS_VAR_0.includes("user_uuids")?" People are named in `people` as the person described them; the host resolves them, never the model.":""}
