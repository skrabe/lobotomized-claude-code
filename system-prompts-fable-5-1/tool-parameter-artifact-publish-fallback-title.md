<!--
name: 'Tool Parameter: Artifact Publish Fallback Title'
description: >-
  Artifact tool title parameter used as fallback when the HTML file has no
  <title>.
ccVersion: 2.1.261
variables:
  - TOOL_PARAMETER_ARTIFACT_PUBLISH_FALLBACK_TITLE_VAR_0
-->
publish: fallback title for an HTML page whose file has no <title> (a name, not a summary; keep it stable across redeploys).${TOOL_PARAMETER_ARTIFACT_PUBLISH_FALLBACK_TITLE_VAR_0.typeCreateOn?" On a `type_url` create: the new Artifact's name — what the user called it, or a short descriptive name; left out, it is named after the type.":""}
