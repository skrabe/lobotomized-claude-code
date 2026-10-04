<!--
name: 'Slash Command: Plugin Marketplace Remove Plugins Turned Off Commit Mismatch'
description: >-
  Result note after removing a marketplace entry: names the plugins turned off
  because they are not at the commit the built-in marketplace lists, and how to
  reinstate one (claude plugin update, then enable).
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_1
  - >-
    SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_2
-->
Turned off ${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_0}: not at the commit the ${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_1} lists. To use one again: claude plugin update <id>, then claude plugin enable <id>.${SLASH_COMMAND_PLUGIN_MARKETPLACE_REMOVE_PLUGINS_TURNED_OFF_COMMIT_MISMATCH_VAR_2}
