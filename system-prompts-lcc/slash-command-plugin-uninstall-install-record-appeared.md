<!--
name: 'Plugin Uninstall: Install Record Appeared During Switch-Off'
description: >-
  Uninstall refusal when an install record appeared while the plugin was being
  switched off, or the install records could no longer be read; nothing it saved
  was removed and the user should run uninstall again.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_INSTALL_RECORD_APPEARED_VAR_0
-->
"${SLASH_COMMAND_PLUGIN_UNINSTALL_INSTALL_RECORD_APPEARED_VAR_0}" was not removed: an install record for it appeared while it was being switched off, or the install records could no longer be read. Nothing it saved was removed. Run the uninstall again.
