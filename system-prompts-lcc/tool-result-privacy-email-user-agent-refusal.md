<!--
name: 'Hook denial: email with User-Agent'
description: >-
  Deny reason from the privacy builtin hook for a shell call holding the account
  email and a User-Agent.
ccVersion: 2.1.322
-->
This call was refused: it holds the account's email address and what looks like a User-Agent setting. If nobody asked to send the address, run it again without it, with a generic client name. Otherwise run it again without that setting, or run the two in separate calls.
