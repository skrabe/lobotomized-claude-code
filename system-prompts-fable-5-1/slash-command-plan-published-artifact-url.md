<!--
name: 'Slash Command: /plan share — plan published'
description: >-
  Tells the model the plan was published as an artifact and gives its URL, which
  the model may need to reference or repeat back to the user.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_PLAN_PUBLISHED_ARTIFACT_URL_VAR_0
-->
Published plan: ${SLASH_COMMAND_PLAN_PUBLISHED_ARTIFACT_URL_VAR_0.url}
