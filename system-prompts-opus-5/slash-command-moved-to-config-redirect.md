<!--
name: 'Slash Command: /vim and /output-style moved into /config'
description: >-
  Tells the model the invoked command no longer exists on its own and names the
  /config tab that replaced it, which is what it must relay to the user.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_MOVED_TO_CONFIG_REDIRECT_VAR_0
  - SLASH_COMMAND_MOVED_TO_CONFIG_REDIRECT_VAR_1
-->
/${SLASH_COMMAND_MOVED_TO_CONFIG_REDIRECT_VAR_0} moved → ${SLASH_COMMAND_MOVED_TO_CONFIG_REDIRECT_VAR_1[t]} in /config
