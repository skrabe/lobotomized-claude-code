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
-->
\`/${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_0}\` was invoked: a request for ${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_1} made as a NEW Artifact from the published Artifact type titled "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2}". Use the \`${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_3}\` tool the way its Artifact-types guidance describes: list the Artifact types available to this user (\`type_query: "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2}"\`), take the listed type whose title is "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2}" (if more than one has that title, ask the user which before creating), create the new Artifact from its \`type_url\` — a \`title\` drawn from the brief, and no files at first so the type's instructions arrive — then fill it by following those instructions. If no type titled "${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_2}" is listed for this user, say so plainly and offer to make ${SLASH_COMMAND_NEW_ARTIFACT_FROM_PUBLISHED_TYPE_VAR_1} another way.
