<!--
name: 'Tool Parameter: Claude in Chrome navigate tabId'
description: >-
  Description of the `tabId` parameter in the claude-in-chrome `navigate` tool's
  inputSchema, sent to the model as part of the browser tool definitions.
ccVersion: 2.1.211
-->
Tab ID to navigate. Must be a tab in the current group. If omitted for URL navigation when calling navigate standalone, tabs_context_mcp{createIfEmpty:true} is called for you. Required for url:"back"/"forward" and for navigate (and other tools that act on a page) inside browser_batch.
