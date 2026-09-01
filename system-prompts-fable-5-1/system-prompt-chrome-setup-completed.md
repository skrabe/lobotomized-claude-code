<!--
name: 'System prompt: Chrome setup completed'
description: >-
  Model-facing browser-preload text block, a backtick template prepended to the
  base Chrome-automation prompt ${KZt}, telling the model the extension is
  installed and browser tools are now available
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_CHROME_SETUP_COMPLETED_VAR_0
-->
Claude in Chrome setup completed: the extension is installed and connected, and the mcp__claude-in-chrome__* browser tools are now available in this session. Continue the user's task using them.

${SYSTEM_PROMPT_CHROME_SETUP_COMPLETED_VAR_0}
