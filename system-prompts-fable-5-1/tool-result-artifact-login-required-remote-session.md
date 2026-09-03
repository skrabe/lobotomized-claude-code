<!--
name: 'Tool Result: Artifact login required (remote session)'
description: >-
  Artifact tool validation/call error returned to the model when the remote
  session's launching machine is not signed in to claude.ai.
ccVersion: 2.1.224
-->
Artifacts need a claude.ai login, and this remote session authenticates through the machine that launched it, which is not signed in to claude.ai. Sign in to claude.ai on that machine (/login, "Claude account with subscription"), then reconnect this session.
