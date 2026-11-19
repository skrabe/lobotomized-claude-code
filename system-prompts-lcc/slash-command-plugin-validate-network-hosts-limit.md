<!--
name: 'Slash Command: /plugin validate — network hosts over limit'
description: >-
  Validation warning that only the first N network hosts are read and the rest
  are ignored at load time.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_NETWORK_HOSTS_LIMIT_VAR_0
-->
Only the first ${SLASH_COMMAND_PLUGIN_VALIDATE_NETWORK_HOSTS_LIMIT_VAR_0} entries are read. The rest will be ignored at load time.
