<!--
name: /design and /slides New Artifact From Published Type
description: >-
  Slash-command prompt telling the model a /design or /slides invocation is a
  request to create a new artifact from a published Artifact type: list types,
  pick the titled type, create from type_url, then fill from the brief.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_0
  - SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_1
  - SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2
  - SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_3
  - SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_2_VAR_4
-->
\`/${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_0}\` was invoked: a request for ${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_1} made as a NEW Artifact from the published Artifact type titled "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2}". Call the \`${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_3}\` tool with \`action: "quickstart"\` and \`intent: "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_2_VAR_4}"\` (adding \`design_systems: false\` if you already have a design system's link or the user declined one), then do what its result says: create the new Artifact from the type it names — a \`title\` drawn from the brief, and no files at first so the type's instructions arrive — and fill it by following those instructions. If it says no such type is listed for this user, say so plainly, then do what it says instead.
