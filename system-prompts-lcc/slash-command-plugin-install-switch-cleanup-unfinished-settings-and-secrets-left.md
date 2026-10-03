<!--
name: >-
  Slash Command: /plugin Install — Switch Cleanup Unfinished, Settings And
  Secrets Left
description: >-
  Note appended to the plugin switch result saying the cleanup after the last
  uninstall did not finish, so the plugin's settings and stored secrets may
  still be left and no command removes them yet
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_CLEANUP_UNFINISHED_SETTINGS_AND_SECRETS_LEFT_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_CLEANUP_UNFINISHED_SETTINGS_AND_SECRETS_LEFT_VAR_1
-->
${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_CLEANUP_UNFINISHED_SETTINGS_AND_SECRETS_LEFT_VAR_0}its settings may still be under "pluginConfigs" in your user settings file, and its stored secrets in ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCH_CLEANUP_UNFINISHED_SETTINGS_AND_SECRETS_LEFT_VAR_1}. No command removes them for this id yet; you can take that entry out yourself; the stored secrets stay
