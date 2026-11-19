<!--
name: '/plugin install: installed but plugin is off'
description: >-
  Install result message noting the installed plugin is off by default or in
  settings, with the enable hint.
ccVersion: 2.1.328
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_2
-->
${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_0}${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_1} This plugin is off ${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_2.disabled==="by-default"?"by default":"in your settings"}. ${SLASH_COMMAND_PLUGIN_INSTALL_INSTALLED_PLUGIN_OFF_NOTE_VAR_2.enableHint}
