<!--
name: 'Tool Description: Claude in Chrome bridge disconnect error'
description: >-
  Error message shown when a Claude in Chrome tool call fails because the Chrome
  extension disconnects mid-operation
ccVersion: 2.1.178
variables:
  - CHROME_TOOL_NAME
-->
The "${CHROME_TOOL_NAME}" tool call failed because the Chrome extension disconnected mid-operation. Retry in a few seconds. If it keeps failing, ask the user to switch to Chrome (which wakes the extension) or check that the extension is still logged in.
