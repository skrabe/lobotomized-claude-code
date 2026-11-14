<!--
name: 'Tool whenToUse: Computer use setup'
description: >-
  Deferred-tool listing line telling Claude to call the computer-use setup tool
  once when asked to work in desktop apps without computer tools.
ccVersion: 2.1.325
variables:
  - TOOL_WHEN_TO_USE_COMPUTER_USE_SETUP_VAR_0
-->
When the user asks you to work in an application on their computer, or to use their computer or screen, and you have no mcp__${TOOL_WHEN_TO_USE_COMPUTER_USE_SETUP_VAR_0}__computer_ tools, use it once first; not for work needing only their web browser.
