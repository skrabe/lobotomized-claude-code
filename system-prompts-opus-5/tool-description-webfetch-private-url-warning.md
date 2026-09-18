<!--
name: 'Tool Description: WebFetch private URL warning'
description: >-
  WebFetch usage warning — the tool fails on authenticated or private URLs;
  check whether the URL points to an authenticated service and prefer a
  specialized MCP tool, with the claude.ai artifact-URL exception
ccVersion: 2.1.277
variables:
  - FORMAT_ARTIFACT_LINK_NOTE_FN
  - ARTIFACT_LINK_HANDLING_MODE
  - WEBFETCH_TOOL_DESCRIPTION_BLOCK_FN
-->
${WEBFETCH_TOOL_DESCRIPTION_BLOCK_FN()}
