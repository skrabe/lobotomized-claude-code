<!--
name: 'Slash Command: /chrome — couldn''t switch browser'
description: >-
  /chrome result when switching the browser used for Chrome actions fails, with
  the error message.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_CHROME_SWITCH_BROWSER_FAILED_VAR_0
  - SLASH_COMMAND_CHROME_SWITCH_BROWSER_FAILED_VAR_1
-->
Couldn't switch browser: ${SLASH_COMMAND_CHROME_SWITCH_BROWSER_FAILED_VAR_0(SLASH_COMMAND_CHROME_SWITCH_BROWSER_FAILED_VAR_1).message}
