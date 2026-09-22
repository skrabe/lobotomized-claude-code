<!--
name: 'Slash Command: /web-setup — server error, retry later'
description: >-
  Tells the model the failure was server-side with its HTTP status and that
  retrying shortly is the right response, rather than changing the request.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_WEB_SETUP_SERVER_ERROR_RETRY_VAR_0
-->
Server error (${SLASH_COMMAND_WEB_SETUP_SERVER_ERROR_RETRY_VAR_0.status}). Try again in a moment.
