<!--
name: Whiteboard publish needs artifact capability
description: >-
  Artifact-publish error telling the model a whiteboard page was published
  without the `artifact` capability its Send-to-Claude button needs.
ccVersion: 2.1.232
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_WHITEBOARD_NEEDS_ARTIFACT_CAPABILITY_VAR_0
-->
This page is a whiteboard, and its Send to Claude button works only through the \`artifact\` capability (artifact publish; legacy spelling \`self\`), which this publish does not declare. ${TOOL_RESULT_ARTIFACT_PUBLISH_WHITEBOARD_NEEDS_ARTIFACT_CAPABILITY_VAR_0===void 0?"Re-run this same publish passing `capabilities: {artifact: {}}` (include `downloads: {}` as well only if the `artifact-capabilities` roster lists it for this user), keeping every other input the same.":"Re-run this same publish with `artifact: {}` added to the `capabilities` you passed, keeping the rest of that declaration and every other input the same."}
