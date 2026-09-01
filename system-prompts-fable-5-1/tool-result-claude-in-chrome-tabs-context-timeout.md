<!--
name: 'Tool Result: Claude in Chrome tabs_context_mcp Timeout'
description: >-
  Tool-result error returned to the model when the front-loaded tabs_context_mcp
  lookup for a standalone navigate call times out, telling it to retry or call
  tabs_context_mcp explicitly.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_CLAUDE_IN_CHROME_TABS_CONTEXT_TIMEOUT_VAR_0
-->
The hidden tabs_context_mcp lookup did not respond within ${TOOL_RESULT_CLAUDE_IN_CHROME_TABS_CONTEXT_TIMEOUT_VAR_0/1000}s. The Chrome extension may be slow to start or waiting on a permission prompt. Retry navigate, or call tabs_context_mcp explicitly to get a tabId first.
