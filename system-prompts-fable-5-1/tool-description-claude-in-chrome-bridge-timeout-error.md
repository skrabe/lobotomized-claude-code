<!--
name: 'Tool Description: Claude in Chrome bridge timeout error'
description: >-
  Error message shown when a Claude in Chrome tool does not respond before
  timing out
ccVersion: 2.1.178
variables:
  - CHROME_TOOL_NAME
-->
The "${CHROME_TOOL_NAME}" tool did not respond in time. The Chrome extension is connected but the page may be loading, unresponsive, or waiting on a permission prompt in the extension side panel. Try a lighter operation (e.g., "get_page_text" instead of a screenshot) or ask the user to check the page and any pending prompts.
