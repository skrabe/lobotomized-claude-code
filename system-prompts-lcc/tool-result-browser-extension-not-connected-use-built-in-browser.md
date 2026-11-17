<!--
name: 'Tool result: browser extension not connected, use built-in browser'
description: >-
  Chrome tool result when the extension is not connected, steering to the
  built-in browser unless the user asked for Chrome.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_BROWSER_EXTENSION_NOT_CONNECTED_USE_BUILT_IN_BROWSER_VAR_0
-->
Browser extension is not connected. Continue the task in the built-in browser now, with no Chrome setup steps, unless the user asked for Chrome in this conversation, by name or by description (a saved Preferred browser setting does not count), or the task needs something only their Chrome has, such as an open tab. In that case, tell them briefly that Chrome is not connected and that to connect it they open Chrome with the extension (${TOOL_RESULT_BROWSER_EXTENSION_NOT_CONNECTED_USE_BUILT_IN_BROWSER_VAR_0}) signed in to this Claude account, offer the built-in browser unless they refused it or it cannot help, and stop until they reply.
