<!--
name: 'Tool Description: WebFetch private URL warning'
description: >-
  WebFetch usage warning — the tool fails on authenticated or private URLs;
  check whether the URL points to an authenticated service and prefer a
  specialized MCP tool, with the claude.ai artifact-URL exception
ccVersion: 2.1.233
variables:
  - IS_ARTIFACT_TOOL_ENABLED
  - WEBFETCH_TOOL_DESCRIPTION_BLOCK
-->
${WEBFETCH_TOOL_DESCRIPTION_BLOCK()}
