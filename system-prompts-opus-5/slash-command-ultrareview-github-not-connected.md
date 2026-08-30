<!--
name: 'Slash Command: Ultrareview GitHub Not Connected'
description: >-
  Ultrareview launch error when no GitHub account is connected to the Claude
  account, with recovery steps.
ccVersion: 2.1.251
variables:
  - SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_2
  - SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_3
-->
Ultrareview clones ${SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_0} in the cloud with the GitHub account connected to your Claude account, and none is connected (or the connection expired). To fix: ${SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_1?`${SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_1}, or connect`:"connect"} an account at ${SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_2} — ${SLASH_COMMAND_ULTRAREVIEW_GITHUB_NOT_CONNECTED_VAR_3} (allow a minute after connecting).
