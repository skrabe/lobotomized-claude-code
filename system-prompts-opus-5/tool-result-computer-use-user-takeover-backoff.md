<!--
name: 'Tool Result: Computer Use User Takeover Backoff'
description: >-
  Tells the model that the user took over an app and background control is
  backing off for N more seconds.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_USER_TAKEOVER_BACKOFF_VAR_0
  - TOOL_RESULT_COMPUTER_USE_USER_TAKEOVER_BACKOFF_VAR_1
-->
${TOOL_RESULT_COMPUTER_USE_USER_TAKEOVER_BACKOFF_VAR_0.ceil(TOOL_RESULT_COMPUTER_USE_USER_TAKEOVER_BACKOFF_VAR_1/1000)}s. Wait, work on something else, or ask the user.
