<!--
name: 'Slash Command: /context — remote fetch failed'
description: >-
  Reports that the remote control-channel request for context usage threw, so
  the model knows the figures are missing because of a transport failure rather
  than because usage is zero.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_CONTEXT_REMOTE_FETCH_FAILED_VAR_0
  - SLASH_COMMAND_CONTEXT_REMOTE_FETCH_FAILED_VAR_1
-->
Couldn't fetch context from remote: ${SLASH_COMMAND_CONTEXT_REMOTE_FETCH_FAILED_VAR_0(SLASH_COMMAND_CONTEXT_REMOTE_FETCH_FAILED_VAR_1)}
