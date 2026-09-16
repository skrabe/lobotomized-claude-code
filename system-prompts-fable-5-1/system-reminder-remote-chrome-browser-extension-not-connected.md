<!--
name: 'System Reminder: Remote Chrome browser extension not connected'
description: >-
  Explains that Chrome on the user's computer cannot be reached and directs the
  user to check Chrome, the extension, and account sign-in
ccVersion: 2.1.273
variables:
  - CHROME_EXTENSION_URL
-->
Browser extension is not connected. Chrome on the user's computer could not be reached from this session: that computer may be closed or asleep, Chrome may not be running there, the Claude extension may not be installed there (${CHROME_EXTENSION_URL}), or this session may not be able to connect to Chrome. Ask the user to make sure that computer is awake and Chrome is open there with the Claude extension, then retry. If it still fails, ask the user to check that the extension is signed in to the same claude.ai account they use here.
