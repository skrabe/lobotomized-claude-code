<!--
name: 'Data: Chrome install started, continuing without browser'
description: >-
  Model-facing outcome message returned (var udb) when the user began installing
  the Claude in Chrome extension but chose to continue without browser tools,
  injected into the model's context so it stops suggesting the extension and
  proceeds
ccVersion: 2.1.206
-->
The user started installing the Claude in Chrome extension but chose to continue without browser tools. Do not suggest the extension again this session. Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. If they finish installing later, /chrome completes the connection, and the next Claude Code session detects the extension automatically.
