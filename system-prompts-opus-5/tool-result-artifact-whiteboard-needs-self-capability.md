<!--
name: Artifact Whiteboard Needs Self Capability
description: >-
  Thrown by xlp() as an ArtifactInputError (reasonCode
  whiteboard_needs_self_capability) and returned to the model as an is_error
  tool_result when a whiteboard page is published without declaring the `self`
  capability.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_ARTIFACT_WHITEBOARD_NEEDS_SELF_CAPABILITY_VAR_0
-->

This page is a whiteboard, and its Send to Claude button works only through the \`self\` capability, which this publish does not declare — shipping it would put up a board that can never send back. ${TOOL_RESULT_ARTIFACT_WHITEBOARD_NEEDS_SELF_CAPABILITY_VAR_0===void 0?"Re-run this same publish passing `capabilities: {self: {}}` (include `downloads: {}` as well only if the `artifact-capabilities` roster lists it for this user), keeping every other input the same.":"Re-run this same publish with `self: {}` added to the `capabilities` you passed, keeping the rest of that declaration and every other input the same."}
