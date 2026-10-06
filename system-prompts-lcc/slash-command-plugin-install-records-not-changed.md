<!--
name: '/plugin install: installed_plugins.json not changed'
description: >-
  Refusal when installed_plugins.json holds records this build cannot read, so
  the install record is not written
ccVersion: 2.1.291
variables:
  - SLASH_COMMAND_PLUGIN_INSTALL_RECORDS_NOT_CHANGED_VAR_0
  - SLASH_COMMAND_PLUGIN_INSTALL_RECORDS_NOT_CHANGED_VAR_1
-->
installed_plugins.json was not changed: ${SLASH_COMMAND_PLUGIN_INSTALL_RECORDS_NOT_CHANGED_VAR_0??SLASH_COMMAND_PLUGIN_INSTALL_RECORDS_NOT_CHANGED_VAR_1({unreadRecordIds:e,formatVersion:n})}
