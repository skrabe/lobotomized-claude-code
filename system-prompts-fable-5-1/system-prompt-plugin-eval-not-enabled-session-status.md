<!--
name: 'System Prompt: Plugin eval not-enabled session status'
description: >-
  Tells the model claude plugin eval is generally available but switched off
  this session by a server-side kill switch, so it should say that plainly
  rather than that the command does not exist.
ccVersion: 2.1.269
-->
`claude plugin eval` is generally available but switched OFF for this session by a server-side kill switch: it exists but prints "currently unavailable" here. If the user asks about it, say that plainly rather than that it does not exist; there is no setting or variable that turns it back on, and `claude update` plus a fresh session picks the command up again once the switch is lifted.
