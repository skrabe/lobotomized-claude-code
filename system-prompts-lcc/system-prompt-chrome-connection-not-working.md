<!--
name: 'System prompt: Chrome connection not working'
description: >-
  Model-facing browser-preload text block (returned as [{type:'text',text:o}])
  telling the model the Chrome connection failed/disabled so
  mcp__claude-in-chrome__* tools are unavailable and to continue without them
ccVersion: 2.1.291
-->
Claude in Chrome is enabled for this session, but the browser connection is not working (it failed or was disabled), so mcp__claude-in-chrome__* tools are not available. Do not attempt them. Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. The user can restart the connection with /chrome (Reconnect extension), or turn Claude in Chrome back on in /mcp if it was turned off there.
