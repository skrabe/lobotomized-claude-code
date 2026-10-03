<!--
name: 'Slash Command: Plugin Install — Switched But Disabled Note'
description: >-
  Sentence appended to the successful switch result telling the reader the
  plugin is disabled in their settings and how to enable it.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_1
  - SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_2
-->
. ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_1)} is disabled in your settings — enable it ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_2?`with: ${SLASH_COMMAND_PLUGIN_INSTALL_SWITCHED_BUT_DISABLED_NOTE_VAR_2}`:"in /plugin"}
