<!--
name: 'Tool whenToUse: Desktop app browser setup'
description: >-
  Deferred-tool listing line telling Claude to call the desktop-app browser
  setup tool once, and the Chrome tool for the user's Chrome.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_DESKTOP_BROWSER_SETUP_VAR_0
-->
When the user asks you to work in the Claude desktop app's own browser or on a website needing their sign-in, and you have no tools for that browser yet, use it once; for their Chrome, use ${TOOL_WHEN_TO_USE_DESKTOP_BROWSER_SETUP_VAR_0}.
