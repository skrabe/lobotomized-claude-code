<!--
name: 'Tool Result: Device bridge ask for folder again before retry'
description: >-
  Guidance after a call waited for an attached computer: do not resend yet, look
  up the user's computers and request the folder again, else ask the user to
  check Claude is running
ccVersion: 2.1.319
-->
Do not send this call again yet. If you have not asked for a folder on that computer since that wait, look the user's computer folders up and, if that computer is listed as online, ask for the folder this session was using there (the user approves the request); when it is attached, send the call again. Otherwise, or if the request does not bring the computer back, ask the user to check that Claude is running on that computer.
