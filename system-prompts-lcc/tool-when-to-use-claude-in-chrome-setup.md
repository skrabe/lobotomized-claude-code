<!--
name: 'Tool whenToUse: Claude in Chrome setup'
description: >-
  Deferred-tool listing line telling Claude to call the Chrome setup tool once
  when asked to act in the user's Chrome without Chrome tools.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_CLAUDE_IN_CHROME_SETUP_VAR_0
-->
When the user asks you to act in their own Chrome browser or on a website that needs their sign-in, and you have no Claude in Chrome tools yet, use it once first, not for questions ${TOOL_WHEN_TO_USE_CLAUDE_IN_CHROME_SETUP_VAR_0} can answer.
