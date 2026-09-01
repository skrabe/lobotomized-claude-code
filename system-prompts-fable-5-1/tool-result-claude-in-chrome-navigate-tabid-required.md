<!--
name: 'Tool Result: Navigate Requires tabId For Back/Forward'
description: >-
  Error tool-result returned to the model when it calls the browser navigate
  tool with url:"back"/"forward" without a tabId, directing it to call
  tabs_context_mcp first.
ccVersion: 2.1.211
-->
tabId is required for url:"back"/"forward". Call tabs_context_mcp first to get a tab ID.
