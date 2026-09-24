<!--
name: 'Tool Result: Not An Artifact URL (claude.ai link carrying an artifact)'
description: >-
  Artifact tool validation error when the url is a claude.ai page link that
  carries an artifact slug; tells the model to pass the artifact's own URL in
  the named field.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_0
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_1
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_2
  - TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_3
-->
${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_0} that is a claude.ai ${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_1} link; pass the artifact's own URL (${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_2}) as \`${TOOL_RESULT_ARTIFACT_URL_NOT_AN_ARTIFACT_CLAUDE_AI_ARTIFACT_LINK_VAR_3.field??"url"}\`.
