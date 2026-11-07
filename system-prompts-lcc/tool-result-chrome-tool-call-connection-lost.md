<!--
name: 'Tool result: Chrome tool call connection lost'
description: >-
  Error result telling the model a browser tool call was sent but the connection
  dropped before the result, so it must check page state before repeating
  non-read actions.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_CHROME_TOOL_CALL_CONNECTION_LOST_VAR_0
-->
The "${TOOL_RESULT_CHROME_TOOL_CALL_CONNECTION_LOST_VAR_0}" tool call was sent, but the connection was lost before its result came back. The action may have happened, may still be in progress or waiting for the user in Chrome, or may not have happened. If the call only reads the page, call it again. Otherwise do not repeat it yet: first check the page's current state (for example with "get_page_text" or a screenshot), and repeat the action only if it clearly did not take effect.
