<!--
name: 'Tool result: SendMessage peer auth not claude.ai login'
description: >-
  SendMessage error when this session signs in another way and so cannot message
  sessions on other machines under the claude.ai login.
ccVersion: 2.1.326
-->
auth: this session signs in with an API key, an auth token, a profile or workload identity, so it can't send under your claude.ai login. Messaging other machines needs a session on that login, so a retry won't help. Messages to sessions on this machine still work.
