<!--
name: 'Tool Result: Artifact Publish Private Gallery Hint'
description: >-
  Publish-result tail telling the model artifacts stay private until shared and
  how to reopen them from /artifacts, ctrl+], or the web gallery.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_PRIVATE_GALLERY_HINT_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_PRIVATE_GALLERY_HINT_VAR_1
-->
Artifacts are private unless shared from the page's share menu. To get back to it later: in the Claude Code terminal, /artifacts lists the artifacts you own or were shared (o opens, c copies the link) and ctrl+] (by default) reopens the most recent artifact from this session; on the web, the gallery at ${TOOL_RESULT_ARTIFACT_PUBLISH_PRIVATE_GALLERY_HINT_VAR_0!==""?`${new TOOL_RESULT_ARTIFACT_PUBLISH_PRIVATE_GALLERY_HINT_VAR_1(TOOL_RESULT_ARTIFACT_PUBLISH_PRIVATE_GALLERY_HINT_VAR_0).host}/code/artifacts`:"claude.ai/code/artifacts"} lists them.
