<!--
name: 'Tool Description: Artifact Find From Earlier Sessions'
description: >-
  Artifact prompt section for listing earlier-session artifacts to recover a URL
  before updating.
ccVersion: 2.1.257
variables:
  - TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_2
-->
**To find artifacts from earlier sessions**: pass \`action: "list"\` (optionally with \`limit\` and \`scope\`) to enumerate the user's published artifacts — title, URL, favicon, and last-updated, newest first. Use it when the user refers to a published artifact whose URL you don't have, then follow the update flow above with the URL you found. Artifacts published earlier in THIS session need neither \`action: "list"\` nor \`url\` — calling again with the same file path redeploys them. ${TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_0?TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_1:TOOL_DESCRIPTION_ARTIFACT_FIND_FROM_EARLIER_SESSIONS_VAR_2}
