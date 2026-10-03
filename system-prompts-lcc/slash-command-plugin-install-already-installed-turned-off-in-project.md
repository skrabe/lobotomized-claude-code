<!--
name: 'Slash Command: /plugin install — Already Installed, Turned Off In Project'
description: >-
  Suffix on the 'already installed, nothing to install' result when the plugin
  is turned off in this project and the command did not turn it on, with the
  command or /plugin route to turn it on.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_TURNED_OFF_IN_PROJECT_VAR_0
-->
 The plugin is turned off in this project, and this command did not turn it on. To turn it on${SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_TURNED_OFF_IN_PROJECT_VAR_0===null?", open it in /plugin":` for yourself in this project: ${SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_TURNED_OFF_IN_PROJECT_VAR_0}`}
