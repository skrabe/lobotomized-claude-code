<!--
name: 'Slash Command: /web-setup — connected as user, web app opened'
description: >-
  Tells the model the GitHub token import succeeded, under which GitHub
  username, and that a browser was opened at the Claude web URL — the end state
  the model should report.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_WEB_SETUP_CONNECTED_AND_OPENED_VAR_0
  - SLASH_COMMAND_WEB_SETUP_CONNECTED_AND_OPENED_VAR_1
-->
Connected as ${SLASH_COMMAND_WEB_SETUP_CONNECTED_AND_OPENED_VAR_0.result.github_username}. Opened ${SLASH_COMMAND_WEB_SETUP_CONNECTED_AND_OPENED_VAR_1}
