<!--
name: 'Tool Result: Computer Use Restricted Grant Same-Turn Confirm'
description: >-
  Same-turn confirmation clause appended to restricted request_access denials
  (browser/terminal) so Claude retries immediately.
ccVersion: 2.1.246
-->
This is a one-time confirmation that only lasts for the current turn: if you respond to the user and retry in a later turn, you will get this same message again (it is not a permanent block). The user still approves the grant in the dialog that the retry brings up.
