<!--
name: 'Slash Command: /fast — fast mode turned on'
description: >-
  Tells the model the session just switched to fast mode, optionally naming the
  model it was switched to and the per-Mtok rate, so it knows its own execution
  mode and cost profile changed mid-session.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_FAST_MODE_ENABLED_VAR_0
  - SLASH_COMMAND_FAST_MODE_ENABLED_VAR_1
  - SLASH_COMMAND_FAST_MODE_ENABLED_VAR_2
-->
${SLASH_COMMAND_FAST_MODE_ENABLED_VAR_0} Fast mode ON${SLASH_COMMAND_FAST_MODE_ENABLED_VAR_1} · ${SLASH_COMMAND_FAST_MODE_ENABLED_VAR_2}
